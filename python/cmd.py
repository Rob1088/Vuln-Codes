# cmd_injection.py
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/run")
def run():
    # WARNING: vulnerable to command injection
    cmd = request.args.get("cmd", "ls")
    output = os.popen(cmd).read()
    return "<pre>{}</pre>".format(output)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
