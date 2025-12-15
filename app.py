from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
FILE = "habits.json"

def load():
    with open(FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    data = load()
    name = request.json["name"]
    data[name] = False
    save(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
