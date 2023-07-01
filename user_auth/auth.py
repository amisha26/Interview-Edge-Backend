from flask import Flask, Blueprint, request, jsonify
import uuid
from database.database import Database


auth = Blueprint('auth', __name__)

def auth_route(connection):
    dbObj = Database(connection)

    @auth.route('/login', methods = ['POST'])
    def login():
        # get the username and password
        # check user validity
        # connect to db
        # fetch users from database and check if the username and password matches.
        # if it does return 200 else return signup instead
        try:
            req = request.get_json()
            username, password = req["username"], req["password"]
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            validity = dbObj.selectQuery(query)
            if validity == None:
                return jsonify({"msg" : "Username/Password is incorrect"}), 400
            else:
                query = f"SELECT username from users where username = '{username}'"
                res = dbObj.selectQuery(query)
                if res != None:
                    return jsonify({"msg" : "success", "id" : res[0]}), 200
                else:
                    return jsonify({"msg" : "Something went wrong"}), 400
        except Exception as e:
            print(e)
            return jsonify({"msg": "Something went wrong"}), 500

        


    @auth.route('/signup', methods = ['POST'])
    def signup():
        # if there is a new user
        # fetch the username and password and insert them to the db
        # check if the username and password created is as per the standards or not
        try:
            req = request.get_json()
            username, password = req["username"], req["password"]
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            validity = dbObj.selectQuery(query)
            if validity == None:
                #login
                id = uuid.uuid1().hex
                query = f"INSERT INTO users(user_id, username, password) VALUES ('{id}', '{username}', '{password}')"
                dbObj.executeQuery(query)
                return jsonify({"msg" : "success"}), 200
            else:
                return jsonify({"msg" : "Username already exists"}), 400
        except Exception as e:
            print(e)
            return jsonify({"msg" : "Something went wrong"}), 500
        
    return auth