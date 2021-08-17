from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/test_bridge", methods=["POST"])
def test_bridge():
    data = request.json
    if "update" in data:
        update = data["update"]
    else:
        update = False
    print(f"update field from request: {update}")
    return "Bridge response"


if __name__ == "__main__":

    app.run(host='0.0.0.0')