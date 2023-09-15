from flask import Flask, Blueprint, request, jsonify
from routes.database.database import Database
from routes.explore.explore_db import ExploreDb
import uuid
from datetime import datetime

explore = Blueprint('explore', __name__)



def explore_route(connection):
    dbObj = Database(connection)
    topicObj = ExploreDb(connection)

    # This is get topics
    @explore.route('/topics', methods=['GET'])
    def topic():
        try:
            id = request.args.get("id")
            #finalData = {"data":dummyData,"onGoingTopic":queryRes} 
            finalData = topicObj.getUserTopicData(id)
            return jsonify({"data": finalData, "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500


    
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
            req = request.get_json()
            question_url, level, platform, question_name, topic_name = req["url"], req["level"], req["platform"], req["question"], req["topic"]
            #print(question_url, level, platform, question_name, topic_name)
            query = f"SELECT * FROM questions WHERE question_url = '{question_url}'"
            validity = dbObj.selectQuery(query)
            if validity == None:
                id = uuid.uuid1().hex
                query = f"INSERT INTO questions(question_id, topic_name, question_url, question_name, level, platform) VALUES ('{id}', '{topic_name}', '{question_url}', '{question_name}', '{level}', '{platform}')"
                dbObj.executeQuery(query)
                return jsonify({"msg": "success"}), 200
            else:
                return jsonify({"message": "Question present already", "error": False}), 200
            
            #return jsonify({"data": question_list, "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500
        

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
            #return jsonify({"data": mark_question, "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500

    return explore