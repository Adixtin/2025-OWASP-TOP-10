from flask import Flask, request, jsonify
import sqlite3
from crypto_utils import encrypt_data, decrypt_data

app = Flask(__name__)

DB = "database.db"


def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            encrypted_secret BLOB
        )
    """)
    conn.commit()
    conn.close()


@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    secret = request.json.get("secret")

    encrypted = encrypt_data(secret)

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, encrypted_secret) VALUES (?, ?)",
        (username, encrypted)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "User registered successfully"})


@app.route("/profile/<int:user_id>", methods=["GET"])
def profile(user_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, encrypted_secret FROM users WHERE id = ?",
        (user_id,)
    )
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404

    username, encrypted_secret = user
    decrypted_secret = decrypt_data(encrypted_secret)

    return jsonify({
        "username": username,
        "secret": decrypted_secret
    })


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5004)
