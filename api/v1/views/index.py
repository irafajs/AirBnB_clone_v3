#!/usr/bin/python3
"""
Shebang to make a py script
"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """method to return a json response format"""
    return jsonify({"status": "OK"})
