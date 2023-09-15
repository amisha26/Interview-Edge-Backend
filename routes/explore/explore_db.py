from routes.database.database import Database


class ExploreDb:
    topicMappping = {"twoPointers": "Two Pointers",
                    "strings": "Strings", "arrays": "Arrays","stack":"Stack",
                    "binarySearch":"Binary Search","linkedlist":"Linked List",
                    "tree-1":"Tree - 1","tree-2":"Tree - 2","dp-1":"Dynamic Programming - 1",
                    "heap":"Heap - Priority Queue","dp-2":"Dynamic Programming - 2",
                    "slidingWindow":"Sliding Window"}
    
    def __init__(self, connection):
        self.dbObj = Database(connection)

    def getUserTopicData(self, id):
        query = f"SELECT q.topic_name AS topic_name, COUNT(q.question_id) AS question_count, COUNT(uq.question_id) AS user_question_count FROM questions q LEFT JOIN userquestions uq ON q.question_id = uq.question_id AND uq.user_id = '{id}' GROUP BY q.topic_name ORDER BY q.topic_name;"
        title = self.dbObj.selectQuery(query, False)
        topic_data = []
        for data in title:
            urltitle, total, solved = data[0], data[1], data[2]
            if urltitle in self.topicMappping:
                title_name = self.topicMappping[urltitle]
            formattedData = {"title": title_name, "urlTitle": urltitle, "total": total, "solved": solved}
            topic_data.append(formattedData)
        queryRes = {"data":"name","onGoingTopic":False }
        finalData = {"data":topic_data,"onGoingTopic":queryRes}
        return finalData