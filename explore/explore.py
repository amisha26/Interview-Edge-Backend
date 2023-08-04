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
        "title": "Arrays",
        "urlTitle": "arrays",
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
        "title": "Trees",
        "urlTitle": "trees",
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

question_list = [
    {
    "url": "hello.com",
    "level": "easy",
    "platform": "codeforces",
    "question": "hello",
    "topic": "binarySearch"
}
]

mark_question = [
    {
    "user_id": "9eee6edc2edb11ee8551a6a688ffce9b",
    "question_id": "b2630f441cc111eea5719f9e1997d77b",
    "topic": "arrays"
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
            return jsonify({"data": selectedTopicData, "error": False}), 200
        
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
                return jsonify({"msg" : "success"}), 200
            else:
                return jsonify({"message": "Question present already", "error": False}), 200
            
            #return jsonify({"data": question_list, "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500
        

    @explore.route('/markQuestion', methods=['POST'])
    def markQuestion():
        try: 
            return jsonify({"data": mark_question, "error": False}), 200

        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500

    return explore