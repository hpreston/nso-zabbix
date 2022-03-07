# Cisco NSO Testing External Scripts
Scripts and utilities for performing Cisco NSO testing with Zabbix. 

| File                      | Description |
| ------------------------- | ----------- |
| `setup.sh`                | Bash script to create the Python venv for the scripts |
| `requirements.txt`        | Python requirements file. Used by setup.sh |
| `nso_tests.py`            | Python module containing functions against NSO. Used by `check_*.py` scripts |
| `check_restconf.sh`       | Wrapper bash script for RESTCONF test | 
| `check_restconf.py`       | Python script to test if RESTCONF is running | 
| `check_nso_packages.sh`   | Wrapper bash script for NSO package test | 
| `check_nso_packages.py`   | Python script to test if NSO packages are UP | 

## Installation 
To use these scripts: 

1. They must be copied to the Zabbix server's path for external scripts. This should be `/usr/lib/zabbix/externalscripts` by default. 
2. The Python virtual environment for the tests must be created.  Executing `setup.sh` on the Zabbix server will setup the venv and install all modules listed in `requirements.txt`
    * The venv is installed at `/opt/zabbix_venvs/venv_nso`.  This path is used by the wrapper scripts to activate the venv and run the Python scripts within it. 