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
            return jsonify({"Error":"Missing required fields"}), 400
        
        applications.append(data)
        return jsonify({"message": "Application added"})


    @app.route("/applications/<int:index>", methods =["GET"])
    def get_application(index):
        if index < 0 or index >= len(applications):
            return jsonify({"Error": "Application not found"}), 404
       
        return jsonify(applications[index])
    
    @app.route("/applications/<int:index>",methods = ["DELETE"])
    def delete_application(index):
        if index < 0 or index >= len(applications):
            return jsonify({"Error": "Application not found"}), 404
        
        applications.pop(index)
        return jsonify({"message": "Application deleted"})
    
    @app.route("/applications/<int:index>", methods = ["PUT"])
    def update_applications(index):
        if index < 0 or index >= len(applications):
            return jsonify({"Error": "Application not found"}), 404
        data1 = request.get_json()
        if ("company_name" not in data1 or "role_title" not in data1 or "status" not in data1):
            return jsonify({"Error":"Missing required fields"}), 400
        applications[index] = data1
        return jsonify({"message": "Application updated"})
        
        

        




    

    