# notepad_tracker.py
from flask import Flask, request, render_template, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/open", methods=["POST"])
def open_file():
    path = request.json.get("path")
    if not os.path.exists(path):
        return jsonify({"error": "File does not exist"}), 404
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return jsonify({"content": content})

@app.route("/save", methods=["POST"])
def save_file():
    path = request.json.get("path")
    content = request.json.get("content")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    # Track changes with Git
    try:
        subprocess.run(["git", "add", path], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-save note"], check=True)
    except:
        pass  # If git is not initialized, just skip
    return jsonify({"message": "Saved!"})

@app.route("/new", methods=["POST"])
def new_file():
    path = request.json.get("path")
    if os.path.exists(path):
        return jsonify({"error": "File already exists"}), 400
    with open(path, "w", encoding="utf-8") as f:
        f.write("")  # Create empty file
    return jsonify({"message": "File created!"})

if __name__ == "__main__":
    app.run(debug=True)
#new comment added