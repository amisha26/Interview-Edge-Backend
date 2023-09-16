from flask import Flask, Blueprint, request, jsonify
from routes.database.database import Database
from routes.profile.profile_db import ProfileDb

# File imports
from mock_apis.profile_mock_api import user_data, dropdown, table

profile = Blueprint('profile', __name__)


def profile_route(connection):
    dbObj = Database(connection)
    profileObj = ProfileDb(connection)


    @profile.route('/user_status', methods=['GET'])
    def user_status():
        try:
            id = request.args.get('id')
            query = f"SELECT q.level, COUNT(*) AS level_count, COUNT(DISTINCT uq.question_id) FROM questions q LEFT JOIN userquestions uq ON q.question_id = uq.question_id WHERE uq.user_id = '{id}' or uq.user_id IS NULL GROUP BY q.level"
            queryRes = dbObj.selectQuery(query, False)
            query1 = f"SELECT count(q.question_id), count(uq.userquestions_id) FROM questions q LEFT JOIN userquestions uq ON q.question_id = uq.question_id"
            queryRes1 = dbObj.selectQuery(query1, False)
            print(queryRes)
            print(queryRes1)
            total, totalSolved = queryRes1[0][0], queryRes1[0][1]
            for data in queryRes:
                if data[0] == "easy":
                    easyTotal = data[1]
                    easySolved = data[2]
                elif data[0] == "medium":
                    mediumTotal = data[1]
                    mediumSolved = data[2]
                elif data[0] == "hard":
                    hardTotal = data[1]
                    hardSolved = data[2]
            user_data1 = {"easySolved": easySolved, "easyTotal": easyTotal, "hardSolved": hardSolved, "hardTotal": hardTotal, "mediumSolved": mediumSolved, "mediumTotal": mediumTotal, "total": total, "totalSolved": totalSolved}
            return jsonify({"data": user_data1, "error": False}), 200
            #return jsonify({"data": user_data1, "error": False}), 200

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
            finalData = profileObj.getTableData(id)
            return jsonify({"data": finalData, "error": False}), 200   
            #return jsonify({"data": table, "error": False}), 200
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500

    return profile
