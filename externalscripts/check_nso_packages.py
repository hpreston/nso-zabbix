#! /usr/bin/env python
"""
A script to test to see if all NSO packages are UP

Author: Hank Preston 
"""

from nso_tests import check_packages_operstatus


# Script entry point
if __name__ == "__main__":
    import argparse

    # Use argparse to determine the host to check : https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description="Test RESTCONF Functional")
    parser.add_argument("--host", type=str, help="Network host to test")
    parser.add_argument(
        "--username", type=str, help="Username to use for connection test"
    )
    parser.add_argument(
        "--password", type=str, help="Password to use for connection test"
    )
    parser.add_argument(
        "--port", type=int, help="The port RESTCONF runs on. Default 443", default=443
    )
    args = parser.parse_args()

    if args.host is None or args.username is None or args.password is None:
        print(
            f"Missing required parameters for test. host={args.host}, username={args.username}"
        )
        exit(1)

    result = check_packages_operstatus(
        args.host, args.username, args.password, args.port
    )
    print(f"{result[0]}: {result[1]}")
