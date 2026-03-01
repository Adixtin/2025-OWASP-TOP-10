## Vulnerability Overview
The application relies on a JSON file for user roles and access levels.  
An attacker can modify the file to escalate privileges or access sensitive data because the application does not verify the integrity of the file before using it.

## Exploitation / Tampering
1. Start the app `python app.py`
2. Open the login page `http://localhost:5000`
3. Login as a normal user `Username: alice`
	- App says that the alice is a regular user
4. Temper JSON file:
```json
{
    "users": [
        {"username": "admin", "role": "admin"},
        {"username": "alice", "role": "admin"},   # <-- role changed!
        {"username": "bob", "role": "user"}
    ]
}
```
5. Login again as alice
	- App now shows that alice is an admin

## Impact
- Users can escalate privileges by modifying the config file
- Sensitive functionality (admin only pages) can be accessed without authorization
- Shows how blind trust of data or software integrity leads to compromise

## Mitigation
1. Verify critical data
	- Use digital signatures or cryptographic hashes to ensure integrity
2. Restrict file access
	- Only admin/root should be able to write config files
3. Use environment-based role assignment
	- Avoid storing critical roles in user-editable files
4. Immutable or signed configs
	- Store signed JSON or use secure vaults for critical data
