from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "<h2>filename:</h2>" \
           "<form method='GET' action='/read'>" \
           "Filename: <input name='file'><br>" \
           "<button type='submit'>Read</button></form>"


@app.route("/read")
def read_file():
    filename = request.args.get("file")

    with open(f"files/{filename}", "r") as f:
        return f"<pre>{f.read()}</pre>"


app.run(debug=True, host="0.0.0.0", port=5006)
