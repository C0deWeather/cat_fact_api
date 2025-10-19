#!/usr/bin/env python3
from datetime import datetime
from flask import Flask, jsonify, abort
import os
import requests

app = Flask(__name__)

user = {
        "email": "frankbright211@gmail.com",
        "name": "Bright Frank",
        "stack": "Python/Flask"
    }


def get_cat_fact():
    try:
        r = requests.get("https://catfact.ninja/fact", timeout=(3,10))

        # Raise exception for http error
        r.raise_for_status()

        return r.json()["fact"]

    except requests.exceptions.Timeout:
        abort(504, description="Request to external API timed out")
    except (
        requests.exceptions.HTTPError,
        requests.exceptions.JSONDecodeError):
        abort(502, description="Bad response from external API")
    except (
        requests.exceptions.RequestException,
        Exception,
        requests.exceptions.ConnectionError):
        abort(500, description="An unexpected error occurred")


@app.get('/me')
def me():
    response = {}
    response["status"] = "success"
    response["user"] = user
    response["timestamp"] = datetime.utcnow().isoformat() + "Z"
    response["fact"] = get_cat_fact()
    return jsonify(response), 200


def error_response(code, e):
    response = {}
    response["status"] = "success"
    response["user"] = user
    response["timestamp"] = datetime.utcnow().isoformat() + "Z"
    response["fact"] = f"could not retrieve cat fact: {str(e)}"
    return jsonify(response), code


@app.errorhandler(504)
def handle_504_error(e):
    return error_response(504, e)


@app.errorhandler(502)
def handle_502_error(e):
    return error_response(502, e)


@app.errorhandler(500)
def handle_500_error(e):
    return error_response(500, e)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
