from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
FILE = "habits.json"


def load_habits():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)


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


@app.route("/complete", methods=["POST"])
def complete_habit():
    habits = load_habits()
    name = request.json["name"]
    habits[name] = True
    save_habits(habits)
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)
