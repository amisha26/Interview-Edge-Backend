# flask imports
from flask import Flask, Blueprint, request, jsonify

# file imports
from routes.database.database import Database
from routes.explore.explore_db import ExploreDb

# library imports
import uuid
from datetime import datetime


explore = Blueprint('explore', __name__)


# ==================== Explore Route =====================
def explore_route(connection):
    dbObj = Database(connection)
    topicObj = ExploreDb(connection) 

    # This is get Topics. It fetches all the topics existing in the db
    @explore.route('/topics', methods=['GET'])
    def topic():
        try:
            # request
            id = request.args.get("id")
            # data manipulation
            finalData = topicObj.getUserTopicData(id)
            # response
            return jsonify({"data": finalData, "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500


    # This is selected topic. It fetches all the questions of the topic selected by the user
    @explore.route('/selected_topic', methods=['GET'])
    def getSelectedTopic():
        try:
            id, topic = request.args.get("id"), request.args.get("topic")
            selectedTopicData1 = topicObj.getUserSelectedTopic(id, topic)
            return jsonify({"data": selectedTopicData1, "error": False}), 200
        
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500


    # Adding questions to questions table
    @explore.route('/add-questions', methods=['POST'])
    def addQuestion():
        try:
            # request
            req = request.get_json()
            question_url, level, platform, question_name, topic_name = req["url"], req["level"], req["platform"], req["question"], req["topic"]
            
            # adding question to the db
            query = f"SELECT * FROM questions WHERE question_url = '{question_url}'"
            validity = dbObj.selectQuery(query)
            # when question does not exist
            if validity == None:
                id = uuid.uuid1().hex
                # insert question into db query
                query = f"INSERT INTO questions(question_id, topic_name, question_url, question_name, level, platform) VALUES ('{id}', '{topic_name}', '{question_url}', '{question_name}', '{level}', '{platform}')"
                dbObj.executeQuery(query)
                # question successfully added response
                return jsonify({"msg": "success"}), 200
            else:
                return jsonify({"message": "Question present already", "error": False}), 200
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500
        

    # This is marking (question solved) and unmarking (question unsolved) the question.
    @explore.route('/markQuestion', methods=['POST'])
    def markQuestion():
        try:
            req = request.get_json()
            user_id, question_id, topic_name = req["user_id"], req["question_id"], req["topic"]
            query = f"SELECT * FROM userQuestions WHERE question_id = '{question_id}' AND topic_name = '{topic_name}' AND user_id = '{user_id}'"
            validity = dbObj.selectQuery(query)
            # when question is marked
            if validity is None:
                id = uuid.uuid1().hex
                date = datetime.now()
                date.strftime("%d/%m/%y")
                query = f"INSERT INTO userQuestions (userQuestions_id, user_id, question_id, topic_name, date) VALUES ('{id}', '{user_id}', '{question_id}', '{topic_name}', '{date}')"
                dbObj.executeQuery(query)
                return jsonify({"data": "Marked question as done", "error": False}), 200
            
            #when question is un-marked
            query = f"DELETE FROM userQuestions WHERE question_id = '{question_id}' AND topic_name = '{topic_name}' AND user_id = '{user_id}'"
            dbObj.executeQuery(query)
            return jsonify({"data": "Question un-marked", "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500

    return explore