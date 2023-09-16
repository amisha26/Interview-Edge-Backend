from routes.database.database import Database

class ProfileDb:
    topicMappping = {"twoPointers": "Two Pointers",
                    "strings": "Strings", "arrays": "Arrays","stack":"Stack",
                    "binarySearch":"Binary Search","linkedlist":"Linked List",
                    "tree-1":"Tree - 1","tree-2":"Tree - 2","dp-1":"Dynamic Programming - 1",
                    "heap":"Heap - Priority Queue","dp-2":"Dynamic Programming - 2",
                    "slidingWindow":"Sliding Window"}
    
    def __init__(self, connection):
        self.dbObj = Database(connection)

    def getTableData(self, id):
        query = f"SELECT q.topic_name, q.question_name, q.question_url, q.level, q.platform, uq.date, CASE WHEN uq.user_id IS NOT NULL THEN TRUE ELSE FALSE END FROM questions q LEFT JOIN userQuestions uq ON q.question_id = uq.question_id AND uq.user_id = '{id}' WHERE (uq.user_id = '{id}' OR uq.user_id IS NULL)"
        queryRes = self.dbObj.selectQuery(query, False)
        rows = []
        for data in queryRes:
            date, done, level, platform, question, url = data[5], data[6], data[3], data[4], data[1], data[2]
            if data[0] in self.topicMappping:
                topic = self.topicMappping[data[0]]
            if done == 1:
                done = "Yes"
            else:
                done = "No"
            formattedData = {"date": date, "done": done, "level": level, "platform": platform, "question": question, "topic": topic, "url": url}
            rows.append(formattedData)
        finalData = {"rows": rows}
        return finalData