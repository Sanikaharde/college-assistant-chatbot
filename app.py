from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("data/responses.json", "r") as file:
    responses = json.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"].lower()

    for keyword, answer in responses.items():

    if keyword.lower() in message:
        return jsonify({
            "response": answer
        })


    return jsonify({
        "response": "Sorry, I don't have information about that."
    })


if __name__ == "__main__":
    app.run(debug=True)