from flask import Flask, request
import json

app = Flask(__name__)

CONFIG_FILE = 'users.json'


def load_users():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)["users"]


def get_user(username):
    users = load_users()
    for user in users:
        if user['username'] == username:
            return user
    return None


@app.route("/")
def home():
    return """
    <h2>Login</h2>
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        <button type="submit">Login</button>
    </form>
    """


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    user = get_user(username)

    if not user:
        return "User not found", 401

    role = user["role"]
    if role == "admin":
        return f"<h2>{username} is admin.</h2>"
    else:
        return f"<h2>{username} is user.</h2>"


app.run(debug=True, port=5007)
