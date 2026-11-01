from flask import Flask, render_template, request, jsonify
import pymssql

app = Flask(__name__)

SERVER = "LAPTOP-707J6I72\\HP"   # change if needed
USER = "sa"
PASSWORD = "YOUR_PASSWORD"
DATABASE = "CollegeChatbot"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"].lower()

    conn = pymssql.connect(
        server=SERVER,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    cursor = conn.cursor(as_dict=True)

    cursor.execute("""
        SELECT keyword, answer
        FROM FAQ
    """)

    rows = cursor.fetchall()

    for row in rows:

        if row["keyword"].lower() in message:

            conn.close()

            return jsonify({
                "response": row["answer"]
            })

    conn.close()

    return jsonify({
        "response": "Sorry, I don't have information about that."
    })


if __name__ == "__main__":
    app.run(debug=True)