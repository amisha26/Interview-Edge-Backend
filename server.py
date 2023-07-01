# Flask imports
from flask import Flask, jsonify
from flask_cors import CORS
# File imports
from user_auth.auth import auth_route
# Library imports
import sqlite3
import atexit

app = Flask(__name__)
CORS(app)


# =============== Database Connection  ===============
def db_connection():
    conn = sqlite3.connect('database.db')
    print('\n connected to database \n')
    return conn

conn = db_connection()
#dbObj = Database(conn)

def close_db_connection():
    print('\n closing database connection \n')
    conn.close()

atexit.register(close_db_connection)
# =============== Database Connection  ===============


# =============== Routes ===============
app.register_blueprint(auth_route(conn), url_prefix='/')


@app.errorhandler(404)
def error(e):
    return jsonify({"msg": "Wrong Route"}), 404


# =============== Routes ===============


if __name__ == '__main__':
    app.run(debug=True, port=5200)