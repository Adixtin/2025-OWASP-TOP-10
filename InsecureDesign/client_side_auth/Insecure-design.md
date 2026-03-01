## Vulnerability concept
- Accepts username and role during login
- Stores role in session
- Grants admin access based purely on user input
- There is no server-side role validation.
- That’s insecure design.

## How to exploit
1. Run the app
	- `python app.py`
2. Open it in the browser
	- `http://localhost:5000`
3. Login with:
	- `name: doesnt matter`
	- `role: admin`
	- Now u have admin access

## Why is this insecure design
- No server-side role assignment
- No database validation
- No access control architecture
- No authorization model

## Mitigation
- Store roles in database
- Assign roles server-side only
- Never accept role from client
- Validate permissions centrally
