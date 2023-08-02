from flask import Flask, Blueprint, request, jsonify
from database.database import Database
import uuid

explore = Blueprint('explore', __name__)

dummyData = [
    {
        "title": "Binary Search",
        "urlTitle": "binarySearch",
        "total": 20,
        "solved": 8
    },
    {
        "title": "Array",
        "urlTitle": "array",
        "total": 30,
        "solved": 4
    },
    {
        "title": "Dynamic Programming",
        "urlTitle": "dynamicProgramming",
        "total": 50,
        "solved": 50
    },    
    {
        "title": "Tree",
        "urlTitle": "tree",
        "total": 25,
        "solved": 10
    }
]

selectedTopicData = [
        {
            "body": [
                {
                    "completed": False,
                    "id": "b2630f441cc111eea5719f9e1997d77b",
                    "name": "Unique Email Addresses",
                    "platform": "leetcode",
                    "url": "https://leetcode.com/problems/unique-email-addresses/"
                },
                {
                    "completed": False,
                    "id": "dcd58f5e1cc111eea5719f9e1997d77b",
                    "name": "Valid Anagram",
                    "platform": "leetcode",
                    "url": "https://leetcode.com/problems/valid-anagram/"
                },
                {
                    "completed": False,
                    "id": "56481cfa1cc511eea5719f9e1997d77b",
                    "name": "Word Pattern",
                    "platform": "leetcode",
                    "url": "https://leetcode.com/problems/word-pattern/"
                }
            ],
            "cardTitle": "Easy",
            "cardType": "easy"
        },
        {
            "body": [
                {
                    "completed": False,
                    "id": "fa5138221cc511eea5719f9e1997d77b",
                    "name": "Valid Sudoku",
                    "platform": "leetcode",
                    "url": "https://leetcode.com/problems/valid-sudoku/"
                }
            ],
            "cardTitle": "Medium",
            "cardType": "medium"
        },
        {
            "body": [
                {
                    "completed": False,
                    "id": "adf148e01cc611eea5719f9e1997d77b",
                    "name": "First Missing Positive",
                    "platform": "leetcode",
                    "url": "https://leetcode.com/problems/first-missing-positive/"
                },
                {
                    "completed": False,
                    "id": "b925f5e41cc611eea5719f9e1997d77b",
                    "name": "Naming a Company",
                    "platform": "leetcode",
                    "url": "https://leetcode.com/problems/naming-a-company/"
                },
                {
                    "completed": False,
                    "id": "2c9f9f50164811eea88ae3300d621ca4",
                    "name": "Trapping Rain Water",
                    "platform": "leetcode",
                    "url": "https://leetcode.com/problems/trapping-rain-water/?envType=list&envId=er2c1j13"
                }
            ],
            "cardTitle": "Hard",
            "cardType": "hard"
        }
    ]

def explore_route(connection):
    dbObj = Database(connection)

    # This is get topics
    @explore.route('/topics', methods=['GET'])
    def topic():
        try:
            queryRes = {"data":"name","onGoingTopic":False }
            finalData = {"data":dummyData,"onGoingTopic":queryRes} 
            return jsonify({"data": finalData, "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500


    
    @explore.route('/selected_topic', methods=['GET'])
    def getSelectedTopic():
        try:
            id, topic = request.args.get("id"), request.args.get("topic")
            print(id, topic)
            return jsonify({"data": selectedTopicData, "error": False}), 200
        
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500


    # This is add questions
    @explore.route('/add-question', methods=['POST'])
    def addQuestion():
        #queryRes = {"data":"name","onGoingTopic":False }
        # finalData = {"data":dummyData,"onGoingTopic":queryRes} 
        # return jsonify({"data": finalData, "error": False}), 200

        try:
            req = request.args()
            topic_name, question_url, question_name, level = req["topic_name"], req["question_url"], req["question_name"], req["level"]
            query = f"SELECT * FROM questions WHERE question_url = '{question_url}'"
            validity = dbObj.selectQuery(query)
            if validity == None:
                id  = uuid.uuid1().hex
                query = f"INSERT INTO questions(question_id, topic_name, question_url, question_name, level) VALUES ('{id}', {topic_name}', '{question_url}', '{question_name}', '{level}')"
                dbObj.executeQuery(query)
                query = f"SELECT topic_name, question_url, question_name, level FROM questions"
                display_questions = dbObj.selectQuery(query)
                question_data = []
                for i in display_questions:
                    question_data.append(i)
                queryRes = {"data":"name","onGoingTopic":False }
                finalData = {"data":question_data,"onGoingTopic":queryRes}
                return jsonify({"data": finalData, "error": False}), 200
            else:
                query = f"SELECT topic_name, question_url, question_name, level FROM questions"
                display_questions = dbObj.selectQuery(query)
                question_data = []
                for i in display_questions:
                    question_data.append(i)
                queryRes = {"data":"name","onGoingTopic":False }
                finalData = {"data":question_data,"onGoingTopic":queryRes}
                return jsonify({"msg": "Question already exists", "data": finalData, "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500

    return explore