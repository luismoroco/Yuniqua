from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=["GET"])
def init_app_page_route():
    return "<h1> Works! </h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
