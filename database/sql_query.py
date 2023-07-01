import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

create_user_table = '''
    CREATE TABLE IF NOT EXISTS users (
    user_id text PRIMARY KEY,
    username text,
    password VARCHAR(25) NOT NULL 
)'''

insert_user = '''
    INSERT INTO users (user_id, username, password)
    VALUES ('101', 'amitej', 'amitej123')
    '''

c.execute(create_user_table)
c.execute(insert_user)

conn.commit()
conn.close()