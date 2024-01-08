#!/usr/bin/python3
"""
Shebang to make a py script
"""


from api.v1.views import app_views
import json
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """method to return a json response format"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """retrieve number of of each objects"""
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User
    datas = [City, Review, User, State, Place, Amenity]
    d_id = ["cities", "reviews", "users", "states", "places", "amenities"]
    obj_arr = {}
    for count in range(len(datas)):
        obj_arr[d_id[count]] = storage.count(datas[count])
    return jsonify(obj_arr)
