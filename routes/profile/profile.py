# flask imports
from flask import Flask, Blueprint, request, jsonify

# file imports
from routes.database.database import Database
from routes.profile.profile_db import ProfileDb
from mock_apis.profile_mock_api import user_data, dropdown, table


profile = Blueprint('profile', __name__)

# ==================== Profile Route =====================
def profile_route(connection):
    dbObj = Database(connection)
    profileObj = ProfileDb(connection)


    # This fetches the status of the user
    @profile.route('/user_status', methods=['GET'])
    def user_status():
        try:
            id = request.args.get('id')
            user_data1 = profileObj.getUserStatus(id)
            return jsonify({"data": user_data1, "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500
        
    # This gives the admin options to add a new question
    @profile.route('/dropdown-data', methods=['GET'])
    def dropdown_data():
        try:
            return jsonify({"data": dropdown, "error": False}), 200
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500
        

    # This displays the questions user has solved
    @profile.route('/table_data', methods = ['GET'])
    def table_data():
        try:
            id = request.args.get('id')
            finalData = profileObj.getTableData(id)
            return jsonify({"data": finalData, "error": False}), 200
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500

    return profile
