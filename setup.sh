#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 BrokenAccessControl/app.py &
python3 CryptographicFailures/crypto_app/app.py & 
python3 Injection/sql_injection/app.py & 
python3 InsecureDesign/client_side_auth/app.py &
python3 AuthFailures/no_acc_lockout/app.py & 
python3 SoftwareOrDataIntegrityFailures/tampered_config/app.py &
python3 SecurityLoggingAndAlertingFailures/logging/app.py &
python3 MisshandlingOfExceptionsConditions/exception/app.py & 
