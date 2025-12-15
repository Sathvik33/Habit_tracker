from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

FILE = "habits.json"

def load_habits():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_habits(habits):
    with open(FILE, "w") as f:
        json.dump(habits, f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/habits", methods=["GET", "POST"])
def habits():
    habits = load_habits()

    if request.method == "POST":
        data = request.json
        habits[data["name"]] = False
        save_habits(habits)
        return jsonify(habits)

    return jsonify(habits)

@app.route("/complete", methods=["POST"])
def complete():
    habits = load_habits()
    name = request.json["name"]
    habits[name] = True
    save_habits(habits)
    return jsonify(habits)

if __name__ == "__main__":
    app.run(debug=True)
