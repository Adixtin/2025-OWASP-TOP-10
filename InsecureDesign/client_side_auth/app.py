from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'specialKey'


@app.route('/')
def home():
    if 'username' in session:
        return f"""
        <h2>Welcome {session['username']}</h2>
        <p>Role: {session['role']}</h2>
        <a href="/admin">Admin</a>
        <a href="/logout">Logout</a>
    """
    return f"""
    <LeftMouse> <h2>Login</h2>
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Role: <input name="role"><br>
        <button type="submit">Login</button>
    </form>
    """


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    role = request.form.get('role')

    session['username'] = username
    session['role'] = role

    return redirect(url_for("home"))


@app.route('/admin')
def admin():
    if "username" not in session:
        return redirect(url_for("home"))

    if session.get('role') == 'admin':
        return "<h1>Admin Panel</h1>"
    else:
        return "<h1>Acces denied</h1>", 403


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("home"))


app.run(debug=True, port=5003)
