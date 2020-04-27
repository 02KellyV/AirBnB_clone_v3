#!/usr/bin/python3
""""""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def _status():
    """returns a JSON file with Status: OK"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def _stats():
    """retrieves the number of each objects by type"""
    objs = {"Amenity": "amenities", "City": "cities", "State": "states",
            "Place": "places", "Review": "reviews", "User": "users"}
    classes = {"Amenity": Amenity, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}
    stats = {}
    for key in objs.keys():
        stats[objs[key]] = storage.count(classes[key])
    return jsonify(stats)
