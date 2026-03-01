from flask import Flask, request, session, redirect, url_for
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "crazyKey"

DB = "database.db"


def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    hashed_pw = hashlib.sha256("batman".encode()).hexdigest()
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
                   ("admin", hashed_pw))
    conn.commit()
    conn.close()


@app.route("/")
def home():
    if "username" in session:
        return f"""
        <h2>Welcome {session['username']}</h2>
        <a href="/dashboard">Dashboard</a><br>
        <a href="/logout">Logout</a>
        """
    return """
    <h2>Login</h2>
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Password: <input type="password" name="password"><br>
        <button type="submit">Login</button>
    </form>
    """


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


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("home"))
    return "<h1>Dashboard - Confidential Data</h1>"


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


init_db()
app.run(debug=True)
