## Vulnerability Overview
The application has login functionality and critical actions, but does not log failed login attempts or suspicious actions, and does not alert administrators, which could result in attacks being unnoticed.

## Demonstration
1. Start the app `python app.py`
2. Attempt multiple failed logins
	- Application returns “Invalid credentials”
	- No record of attempts anywhere

## Impact
- Bruteforce attacks go undetected
- Compromises may remain invisible for long periods
- Forensics and incident response are impossible without logs

## Mitigation
1. Log security relevant events
	- Failed logins, password changes, privilege escalations, critical actions
2. Alert on suspicious activity
	- Notify administrators of repeated failures or abnormal behavior
3. Centralize logs
	- Use a SIEM or logging server to aggregate and analyze logs
4. Protect logs from tampering
	- Make logs read-only for regular users
	- Rotate and archive securely

