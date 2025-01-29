#!/usr/bin/env python3

"""

A python program that retrieves basic information about me

"""


from flask import Flask, Response
from flask_cors import CORS
from datetime import datetime
import json


app = Flask(__name__)
CORS(app)


@app.route("/", strict_slashes=True)
def details():
    details = {
        "email": "donumeh54@gmail.com",
        "current_datetime": datetime.now().isoformat(timespec="seconds") + "Z",
        "github_url": "https://github.com/donumeh/stage_zero",
    }
    response = Response(
        response=json.dumps(details), status=200, mimetype="application/json"
    )
    return response


if __name__ == "__main__":
    app.run()
