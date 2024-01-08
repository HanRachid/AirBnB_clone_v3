#!/usr/bin/python3
"""our routes are defined here
"""
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """returns status
        """
    status = {"status": "ok"}
    return status
