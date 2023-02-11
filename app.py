from flask import Flask
import otisapi

app = Flask(__name__)

@app.route("/")
def hello():
    data = otisapi.elevator_status("unit_001", "USA", "001", "001")
    return str(data)

app.run(host="0.0.0.0", port=5000)