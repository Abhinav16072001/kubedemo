from flask import Flask, jsonify
from connections import coll
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running"})

@app.route("/api/get")
def get_data():
    # Fetch all documents from the collection
    names = coll.find()

    # Convert to list
    result = [name['value'] for name in names if 'value' in name]

    return jsonify({"data": result})


@app.route("/api/add/<name>")
def add_data(name):
    # Insert the name into MongoDB
    coll.insert_one({'value': name})
    return jsonify({"message": f"Added '{name}' successfully"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
