<<<<<<< HEAD
from api.v1.views import app_views
=======
#!/usr/bin/python3
"""Flask index"""
from api.v1.views import app_views
from flask import jsonify
>>>>>>> d70d4032c70c86d9856431acdfb429a8e13b610a


@app_views.route('/status', strict_slashes=False)
def status():
<<<<<<< HEAD
    """returns status
        """
    status = {"status": "ok"}
    return status
=======
    """Returns a JSON string"""
    return jsonify({"status": "OK"})
>>>>>>> d70d4032c70c86d9856431acdfb429a8e13b610a
