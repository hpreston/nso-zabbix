#! /bin/bash 

# Wrapper script for executing RESTCONF test
# 
# Activates the Python venv and calls script passing along 
# arguments.

source /opt/zabbix_venvs/venv_nso/bin/activate
/usr/lib/zabbix/externalscripts/check_restconf.py $*

