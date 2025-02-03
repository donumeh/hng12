#!/usr/bin/env python3

"""

A python program that retrieves basic information about me

"""

from datetime import datetime
import flask
from flask import Flask, Response, request
from flask_cors import CORS
import json
import requests
from typing import Dict
from apis.utils.is_prime import is_prime
from apis.utils.is_perfect import is_perfect
from apis.utils.sum_of_digit import sum_of_digit
from apis.utils.http_requests import request_math
from apis.utils.property import check_property

app = Flask(__name__)
CORS(app)


@app.route("/", strict_slashes=True)
def details() -> flask.wrappers.Response:
    """
    Home Route: Returns details about me
    """
    details: Dict[str, str] = {
        "email": "donumeh54@gmail.com",
        "current_datetime": datetime.now().isoformat(timespec="seconds") + "Z",
        "github_url": "https://github.com/donumeh/stage_zero",
    }
    response = Response(
        response=json.dumps(details), status=200, mimetype="application/json"
    )
    return response


@app.route("/api/classify-number", strict_slashes=True)
def classify_number() -> flask.wrappers.Response:
    """
    classify_number: returns properties of a particular number
    """
    try:
        number: int = int(request.args.get("number"))
        assert isinstance(number, int)
        fact = request_math(number).get("text")
        details: Dict[str, Union[int, str]] = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
			"properties": check_property(number),
            "digit_sum": sum_of_digit(number),
            "fun_fact": fact,
        }
        return Response(
            response=json.dumps(details), status=200, mimetype="application/json"
        )
    except Exception as e:
        error_output: Dict[str, Union[str, bool]] = {
            "number": str(number),
            "error": True,
        }
        print(e)
        return Response(
            response=json.dumps(error_output), status=400, mimetype="application/json"
        )
