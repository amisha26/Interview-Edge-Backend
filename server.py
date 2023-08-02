# Flask imports
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# File imports
from user_auth.auth import auth_route
from explore.explore import explore_route
# Library imports
import sqlite3
import atexit

secret_key = "amisha"

app = Flask(__name__)
CORS(app)

# ==================== JWT Configuration =====================
app.config['JWT_SECRET_KEY'] = secret_key  
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 120
jwt = JWTManager(app)


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
app.register_blueprint(explore_route(conn), url_prefix='/')


@app.errorhandler(404)
def error(e):
    return jsonify({"msg": "Wrong Route"}), 404

# =============== Routes ===============


if __name__ == '__main__':
    app.run(debug=True, port=5200)