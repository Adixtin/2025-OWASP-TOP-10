## Vulnerability Overview
The application has login and file access functionality, but does not handle errors properly:
- Uncaught exceptions crash the application
- Stack traces reveal sensitive information (paths, environment variables, internal logic)
- Attackers can leverage this to gain insight or further exploit the app
Consequences:
- Exposure of server-side paths
- Disclosure of secrets or database structure
- Potential remote code execution if exceptions are mishandled

## Exploitation
1. Run the app `python app.py`
2. Open the page `http://localhost:5000`
3. Enter a non existent filename
	- Browser shows full Flask stack trace
	- Reveals:
		- Full file path on server
		- Python version
		- Application code lines

## Impact
- Attackers can enumerate files and paths
- Sensitive internal information is exposed
- Makes other attacks easier (e.g., path traversal, injection)
- Reveals server and application configuration

## Mitigation
1. Catch exceptions
```python
try:
    with open(f"files/{filename}", "r") as f:
        content = f.read()
except FileNotFoundError:
    return "File not found", 404
except Exception:
    return "An error occurred", 500
```
2. Do not reveal stack traces or internal paths to users
3. Validate user input to prevent unexpected exceptions
4. Log detailed errors internally (server logs) without exposing them to clients
