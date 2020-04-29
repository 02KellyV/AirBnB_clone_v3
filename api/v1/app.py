#!/usr/bin/python3
"""Contains app-flask and endpoints (routes)"""
from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, abort
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def invalid_route(e):
    return (jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def storage_close(issue):
    """calls storage.close()"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', "0.0.0.0")
    port = getenv('HBNB_API_PORT', "5000")
    app.run(host=host, port=port, threaded=True, debug=True)
