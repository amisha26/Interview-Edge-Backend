class Database:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def executeQuery(self, query):    
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()

    def selectQuery(self, query, fetchOne=True):
        cursor = self.connection.cursor()
        cursor.execute(query)
        if fetchOne:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
        return res
    

if __name__ == "__main__":
    pass