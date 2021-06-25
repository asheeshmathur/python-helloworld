from flask import Flask
from flask import json
import logging

app = Flask(__name__)
@app.route('/status')
def healthcheck():
    response=app.response_class(
        response= json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    return response;

@app.route('/metrics')
def metrics():
    response=app.response_class(
        response=json.dumps({"status":"success","Code":0,"data":{"User Count":100}}),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route("/")
def hello():
    return "Om Shri Shri Durga"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
