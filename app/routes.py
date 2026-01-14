from flask import jsonify
from services import applications

def register_routes(app):

    @app.route("/applications", methods=["GET"])
    def get_applications():
        return jsonify(applications)
    