from flask import request, jsonify
from services import applications

def register_routes(app):

    @app.route("/applications", methods=["GET"])
    def get_applications():
        return jsonify(applications)
    
    
    @app.route("/applications", methods = ["POST"])
    def add_application():
        data = request.get_json()
        if  ("company_name" not in data or "role_title" not in data or "status" not in data):
            return jsonify({"error":"Missing required fields"}), 400
        
        applications.append(data)
        return jsonify({"message": "Application added"})

    

    