# Cisco NSO Monitoring for Zabbix

The `nso_template.xml` file contains a Zabbix template to monitor Cisco NSO.  It links to the Linux, Docker and ICMP built-in templates as well as includes NSO specific checks. 


## Requirements

The templates require the a Python virtual environment to be created including the [`requirements.txt`](externalscripts/requirements.txt) Python modules to be installed on the backend host.  A [`setup.sh`](externalscripts/setup.sh) script has been created to build the venv as expected by the external scripts. 

The NSO templates require the external scripts from `externalscripts` to be installed on the backend server.

## Usage

To use these templates, import the XML files and link it to the desired hosts in Zabbix.  

> Note: the templates themselves are tied to the group `Role/Cisco NSO Server - Primary`.

Once linked, go to each host and set the inherited macros for these templates.  You will need to set macro values for: 

* `{$NSO_USERNAME}`
* `{$NSO_PASSWORD}`

Other macros in the template can be set if their values differ from default: 

* `{$NSO_NETCONF_PORT}`: default `830`
* `{$NSO_RESTCONF_PORT}`: default `443`
* `{$NSO_SSH_PORT}`: default `2024`

