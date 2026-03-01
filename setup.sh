#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

printf "\nBroken Access Control \n"
python3 BrokenAccessControl/app.py

printf "\nCryptographic Dailures \n"
python3 CryptographicFailures/crypto_app/app.py

printf "\nInjection \n"
python3 Injection/sql_injection/app.py

printf "\nInsecure Design \n"
python3 InsecureDesign/client_side_auth/app.py

printf "\nAuthentication Failures \n"
python3 AuthFailures/no_acc_lockout/app.py

printf "\nSoftware or Data Integrity Failures \n"
python3 SoftwareOrDataIntegrityFailures/tampered_config/app.py

printf "\nSecurity Logging and Alerting Failures \n"
python3 SecurityLoggingAndAlertingFailures/logging/app.py

printf "\nMishandling of Exceptional Conditions \n"
python3 MisshandlingOfExceptionsConditions/exception/app.py
