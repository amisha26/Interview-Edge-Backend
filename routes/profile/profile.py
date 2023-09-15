from flask import Flask, Blueprint, request, jsonify

profile = Blueprint('profile', __name__)

user_data ={
        "easySolved": 2,
        "easyTotal": 72,
        "hardSolved": 0,
        "hardTotal": 31,
        "mediumSolved": 0,
        "mediumTotal": 144,
        "total": 247,
        "totalSolved": 3
    }



dropdown = [
        {
            "id": "1",
            "label": "Platform",
            "name": "platform",
            "options": [
                {
                    "id": 1,
                    "label": "Codechef",
                    "value": "codechef"
                },
                {
                    "id": 2,
                    "label": "Codeforces",
                    "value": "codeforces"
                },
                {
                    "id": 3,
                    "label": "Leetcode",
                    "value": "leetcode"
                }
            ]
        },
        {
            "id": "2",
            "label": "Level",
            "name": "level",
            "options": [
                {
                    "id": 1,
                    "label": "Easy",
                    "value": "easy"
                },
                {
                    "id": 2,
                    "label": "Medium",
                    "value": "medium"
                },
                {
                    "id": 3,
                    "label": "Hard",
                    "value": "hard"
                }
            ]
        },
        {
            "id": "3",
            "label": "Topic",
            "name": "topic",
            "options": [
                {
                    "id": 1,
                    "label": "Two Pointers",
                    "value": "twoPointers"
                },
                {
                    "id": 2,
                    "label": "Strings",
                    "value": "strings"
                },
                {
                    "id": 3,
                    "label": "Arrays",
                    "value": "arrays"
                },
                {
                    "id": 4,
                    "label": "Stack",
                    "value": "stack"
                },
                {
                    "id": 5,
                    "label": "Binary Search",
                    "value": "binarySearch"
                },
                {
                    "id": 6,
                    "label": "Linked List",
                    "value": "linkedlist"
                },
                {
                    "id": 7,
                    "label": "Tree - 1",
                    "value": "tree-1"
                },
                {
                    "id": 8,
                    "label": "Tree - 2",
                    "value": "tree-2"
                },
                {
                    "id": 9,
                    "label": "Dynamic Programming - 1",
                    "value": "dp-1"
                },
                {
                    "id": 10,
                    "label": "Heap - Priority Queue",
                    "value": "heap"
                },
                {
                    "id": 11,
                    "label": "Dynamic Programming - 2",
                    "value": "dp-2"
                },
                {
                    "id": 12,
                    "label": "Sliding Window",
                    "value": "slidingWindow"
                }
            ]
        }
    ]


table = {
        "rows": [
            {
                "date": None,
                "done": "No",
                "level": "medium",
                "platform": "leetcode",
                "question": "Determine if Two Strings Are Close",
                "topic": "Arrays",
                "url": "https://leetcode.com/problems/determine-if-two-strings-are-close/"
            },
            {
                "date": "2023-08-02 05:49:10",
                "done": "Yes",
                "level": "easy",
                "platform": "leetcode",
                "question": "Count Number of Pairs With Absolute Difference K",
                "topic": "Arrays",
                "url": "https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/"
            },
            {
                "date": "2023-07-30 16:02:42",
                "done": "Yes",
                "level": "easy",
                "platform": "leetcode",
                "question": "Build Array from Permutation",
                "topic": "Arrays",
                "url": "https://leetcode.com/problems/build-array-from-permutation/"
            },
            {
                "date": None,
                "done": "No",
                "level": "medium",
                "platform": "leetcode",
                "question": "Swapping Nodes in a Linked List",
                "topic": "Two Pointers",
                "url": "https://leetcode.com/problems/swapping-nodes-in-a-linked-list/?envType=list&envId=9y4zmb5i"
            },
            {
                "date": None,
                "done": "No",
                "level": "medium",
                "platform": "leetcode",
                "question": "Split Two Strings to Make Palindrome",
                "topic": "Two Pointers",
                "url": "https://leetcode.com/problems/split-two-strings-to-make-palindrome/"
            },
            {
                "date": None,
                "done": "No",
                "level": "medium",
                "platform": "leetcode",
                "question": "3Sum",
                "topic": "Two Pointers",
                "url": "https://leetcode.com/problems/3sum/"
            },
            {
                "date": None,
                "done": "No",
                "level": "medium",
                "platform": "leetcode",
                "question": "Rotate Array",
                "topic": "Two Pointers",
                "url": "https://leetcode.com/problems/rotate-array/"
            }
        ]
    }

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
