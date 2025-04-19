from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Route to serve the landing page
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    # Save submission to a JSON file
    try:
        with open("submissions.json", "a") as file:
            file.write(json.dumps(data) + "\n")
        return jsonify({"status": "success", "message": "Form submitted successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
