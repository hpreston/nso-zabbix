#! /bin/bash 

# Wrapper script for executing NSO packages test
# 
# Activates the Python venv and calls script passing along 
# arguments.
source /opt/zabbix_venvs/venv_nso/bin/activate

# Run Python check-script
/usr/lib/zabbix/externalscripts/check_nso_packages.py $*
