import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# =============== Creating Users Table  ===============
create_user_table = '''
    CREATE TABLE IF NOT EXISTS users (
    user_id text PRIMARY KEY,
    username text,
    password VARCHAR(25) NOT NULL 
)'''

# =============== Inserting dummy users in users table  ===============
insert_user = '''
    INSERT OR IGNORE INTO users (user_id, username, password)
    VALUES ('101', 'amitej', 'amitej123')
    '''


# =============== Creating Questions Table  ===============
create_questions_table = '''
    CREATE TABLE IF NOT EXISTS questions (
    question_id text PRIMARY KEY,
    topic_name VARCHAR(50) NOT NULL,
    question_url VARCHAR(250),
    question_name TEXT NOT NULL,
    level TEXT NOT NULL
        ) '''

# =============== Inserting dummy data in Questions Table  ===============
insert_question = '''INSERT OR IGNORE INTO questions (question_id, topic_name, question_url,
question_name, level)
VALUES ('101', 'binarySearch', 'abc.leetcode.com', 'John and the cows',
'hard')
'''

# =============== Creating userQuestions Table  ===============
create_userQuestions_table = '''
CREATE TABLE IF NOT EXISTS userQuestions (
userQuestions_id TEXT PRIMARY KEY,
user_id TEXT NOT NULL,
question_id text NOT NULL,
topic_name VARCHAR(50) NOT NULL
) '''

# =============== Inserting dummy data in userQuestions Table  ===============
insert_userQuestion = '''INSERT OR IGNORE INTO userQuestions (userQuestions_id, user_id, question_id, topic_name)
VALUES ('101', '2', '11', 'binarySearch')'''


# =============== Executing create table queries  ===============
c.execute(create_user_table)
c.execute(insert_user)
c.execute(create_questions_table)
c.execute(insert_question)
c.execute(create_userQuestions_table)
c.execute(insert_userQuestion)


conn.commit()
conn.close()