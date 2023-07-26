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
    INSERT INTO users (user_id, username, password)
    VALUES ('101', 'amitej', 'amitej123')
    '''


# =============== Creating Questions Table  ===============
create_questions_table = '''
    CREATE TABLE IF NOT EXISTS questions (
            url VARCHAR(25) PRIMARY KEY,
            topic_id text,
            topic VARCHAR(25) NOT NULL,
            question text,
            level VARCHAR(25) NOT NULL,
            platform VARCHAR(25) NOT NULL
        ) '''


# =============== Executing create table queries  ===============
c.execute(create_user_table)
c.execute(insert_user)
c.execute(create_questions_table)

conn.commit()
conn.close()