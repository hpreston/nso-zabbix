"""
Functions used for executing tests related to Cisco NSO.

Author: Hank Preston
"""

import requests


def test_restconf(host, port=443, path="/.well-known/host-meta", verify=False):
    """
    Check to see if a given host is offering RESTCONF services. Test is done
    by requesting the root resource discovery path based on RFC8040
    """

    # if the path doesn't start with a "/", add one
    if path[0:1] != "/":
        path = f"/{path}"

    # if verify=False, silence warnings
    if not verify:
        requests.packages.urllib3.disable_warnings()

    url = f"https://{host}:{port}{path}"

    headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json",
    }

    response = requests.get(url, headers=headers, verify=False)

    return response.status_code


def connect_devices(host, username, password, port=443, verify=False):
    """
    Attempt to connect to all devices in NSO.

    returns (result, details)

    result options:
     - success: All devices that should be connectable, are
     - warning: Some subset of devices that should be connectable
                can't be connected to
     - error: No devices are reachable or NSO unreachable
    """

    result = "success"
    details = ""
    errors = []

    # if verify=False, silence warnings
    if not verify:
        requests.packages.urllib3.disable_warnings()

    url = f"https://{host}:{port}/restconf/data/tailf-ncs:devices/connect"

    headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json",
    }

    response = requests.post(
        url, auth=(username, password), headers=headers, verify=False
    )

    if response.status_code == 200:
        connect_result = response.json()["tailf-ncs:output"]["connect-result"]

        # loop over each device in connect results and process status
        for result in connect_result:
            if not result["result"]:
                if "locked" in result["info"]:
                    # A locked device should NOT be reachable
                    pass
                else:
                    errors.append({"device": result["device"], "info": result["info"]})

        # Set overall status
        if len(errors) > 0:
            result = "warning"
            details = ", ".join([error["info"] for error in errors])

    else:
        result = "error"
        details = f"Request to NSO server returned status: {response.status_code}"

    return (result, details)


def check_packages_operstatus(host, username, password, port=443, verify=False):
    """
    Lookup operational status of all packages from NSO.

    returns (result, details)

    result options:
     - success: All packages are UP
     - warning: Status check returned no data
     - error: Some subset of packages are NOT UP
    """

    result = "success"
    details = "All packages are oper-status: up"
    errors = []

    # if verify=False, silence warnings
    if not verify:
        requests.packages.urllib3.disable_warnings()

    url = f"https://{host}:{port}/restconf/data/tailf-ncs:packages/package?fields=name;oper-status"

    headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json",
    }

    response = requests.get(
        url, auth=(username, password), headers=headers, verify=False
    )

    if response.status_code == 200:
        packages = response.json()["tailf-ncs:package"]

        # loop over each device in connect results and process status
        for package in packages:
            package_name = package["name"]
            oper_status = package["oper-status"].keys()

            if "up" not in oper_status:
                errors.append({"package": package_name, "info": oper_status})

        # Set overall status
        if len(errors) > 0:
            result = "error"
            details = ", ".join(
                [f'{error["package"]} is {error["info"]}' for error in errors]
            )
    elif response.status_code == 204:
        result = "warning"
        details = f"Request for package operational status returned no data."
    else:
        result = "error"
        details = f"Request to NSO server returned status: {response.status_code}"

    return (result, details)
