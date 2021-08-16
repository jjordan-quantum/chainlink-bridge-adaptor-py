from flask import Flask

app = Flask(__name__)


@app.route("/test_bridge")

def test_bridge():
    return "Bridge response"


if __name__ == "__main__":

    app.run(host='0.0.0.0')