from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>/ directory</p>"

@app.route("/download")
def download_files():
    file = request.args.get('file') 
    try:
        f = open('files/'+file)
        return f.read()
    except FileNotFoundError:
        return "file does not exist"
