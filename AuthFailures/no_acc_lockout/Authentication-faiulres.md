## Vulnerability Overview
- The application has a login system, but it is vulnerable to brute-force attacks because:
- No rate limiting is implemented
- No account lockout mechanism exists
- Passwords are hashed but easily brute-forcible offline if leaked
- Sessions do not expire or rotate
- Even though the login looks “secure,” it is easily exploited by automated tools.

## Vulnerable Flask Application
- Login page at /
- Dashboard page at /dashboard
- Passwords stored using SHA256 hash
- No login throttling or lockout
```python
# app.py (excerpt)

# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    hashed_pw = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                   (username, hashed_pw))
    user = cursor.fetchone()
    conn.close()

    if user:
        session["username"] = username
        return redirect(url_for("dashboard"))
    else:
        return "Invalid credentials"
```

## Exploitation
1. Start the application `python app.py`
2. Use a brute forcing tool (for example hydra) to get the login 
```cmd
hydra -l admin -P rockyou.txt 127.0.0.1 -s 5000 http-post-form "/login:username=^USER^&password=^PASS^:Invalid credentials"
```
	- Observe unlimited login attempts succeed if password is weak
	- No lockout or rate limiting prevents Hydra from continuing

## Impact

- Credential guessing / brute-force possible
- Unauthorized access to accounts
- Weak session handling could allow session abuse

## Mitigation

To secure the application:
1. Rate limiting - limit login attempts per user/IP
2. Account lockout - temporarily disable account after X failures
3. Strong password policies - enforce complexity and rotation
4. Multi-factor authentication (MFA) - add a second factor
5. Session management - expire sessions, rotate session IDs, invalidate on logout


