from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
FILE = "habits.json"

def load_habits():
    if not os.path.exists(FILE):
        return {}

    try:
        with open(FILE, "r") as f:
            content = f.read().strip()
            if content == "":
                return {}
            return json.loads(content)
    except:
        return {}


def save_habits(habits):
    with open(FILE, "w") as f:
        json.dump(habits, f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/habits", methods=["GET"])
def get_habits():
    return jsonify(load_habits())

@app.route("/add", methods=["POST"])
def add_habit():
    habits = load_habits()
    name = request.json["name"]
    habits[name] = False
    save_habits(habits)
    return jsonify({"success": True})

@app.route("/toggle", methods=["POST"])
def toggle_habit():
    habits = load_habits()
    name = request.json["name"]
    habits[name] = not habits[name]
    save_habits(habits)
    return jsonify({"success": True})

@app.route("/delete", methods=["POST"])
def delete_habit():
    habits = load_habits()
    name = request.json["name"]
    if name in habits:
        del habits[name]
        save_habits(habits)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)
