from flask import Flask, Blueprint, request, jsonify

# File imports
from mock_apis.profile_mock_api import user_data, dropdown, table

profile = Blueprint('profile', __name__)



def profile_route(connection):

    @profile.route('/user_status', methods=['GET'])
    def user_status():
        try:
            id = request.args.get('id')
            print(id)
            return jsonify({"data": user_data, "error": False}), 200
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500
        

    @profile.route('/dropdown-data', methods=['GET'])
    def dropdown_data():
        try:
            return jsonify({"data": dropdown, "error": False}), 200
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500
        


    @profile.route('/table_data', methods = ['GET'])
    def table_data():
        try:
            id = request.args.get('id')
            print(id)
            return jsonify({"data": table, "error": False}), 200
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500


    return profile
