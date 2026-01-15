from flask import request, jsonify
from services import applications

def register_routes(app):

    @app.route("/applications", methods=["GET"])
    def get_applications():
        return jsonify(applications)
    
    
    @app.route("/applications", methods = ["POST"])
    def add_application():
        data = request.get_json()
        applications.append(data)
        return jsonify({"message": "Application added"})

    

    