from flask import Flask, Blueprint, request, jsonify

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

def explore_route(connection):
    
    @explore.route('/topics', methods=['GET'])
    def topic():
        queryRes = {"data":"name","onGoingTopic":False }
        finalData = {"data":dummyData,"onGoingTopic":queryRes} 
        return jsonify({"data": finalData, "error": False}), 200

    return explore