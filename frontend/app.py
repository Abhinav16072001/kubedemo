from flask import Flask, render_template, jsonify
import os
import requests

app = Flask(__name__)

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://127.0.0.1:8000/')

@app.route("/")
def home():
    env = dict(os.environ)
    return render_template("index.html", env=env)

import requests
from flask import Flask, jsonify

@app.route("/fetch")
def fetch():
    response = requests.get(f"{BACKEND_URL}/api/get")
    data = response.json()
    
    return jsonify({
        "data": data,
        "type": str(type(data))
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
