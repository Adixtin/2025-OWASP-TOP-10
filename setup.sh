#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "BAC"
python3 BrokenAccessControl/app.py 
echo "CF"
python3 CryptographicFailures/crypto_app/app.py 
echo "I"
python3 Injection/sql_injection/app.py 
echo "IS"
python3 InsecureDesign/client_side_auth/app.py 
echo "AF"
python3 AuthFailures/no_acc_lockout/app.py 
echo "SODIF"
python3 SoftwareOrDataIntegrityFailures/tampered_config/app.py 
echo "SLAAF"
python3 SecurityLoggingAndAlertingFailures/logging/app.py 
echo "MOEC"
python3 MisshandlingOfExceptionsConditions/exception/app.py 
