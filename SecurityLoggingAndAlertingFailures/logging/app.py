from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'someKey'

USERS = {
        "admin": "Admin",
        "alice": "password"
}


@app.route('/')
def home():
    return """
      <h2>Login</h2>
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Password: <input type="password" name="password"><br>
        <button type="submit">Login</button>
    </form>
    """


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in USERS and USERS[username] == password:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return 'Invalid credentails'


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))

    return f'<h2>welcome to the dashboard {session["username"]}</h2>'


app.run(debug=True)
