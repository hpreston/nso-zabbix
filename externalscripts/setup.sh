#! /bin/bash 

# Script to setup the Python virtual environment for the 
# NSO tests.

echo "Creating a Python venv for Cisco NSO Checks"
python3.8 -m venv /opt/zabbix_venvs/venv_nso 

echo "Activating Python venv to install requirements"
source /opt/zabbix_venvs/venv_nso/bin/activate
pip install -r requirements.txt 
