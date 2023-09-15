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
    

    def getUserSelectedTopic(self, id, topic):
        #query = f"SELECT q.question_id, q.question_url, q.question_name, q.level, q.platform AS platform, COUNT(uq.question_id) AS user_question_count FROM userQuestions uq RIGHT JOIN questions q ON q.question_id = uq.question_id AND uq.user_id = '{id}' WHERE (uq.user_id = '{id}' OR uq.user_id IS NULL) AND uq.topic_name = '{topic}'"
        query = f"SELECT q.question_url, q.question_id, q.topic_name, q.question_name, q.level, q.platform, CASE WHEN uq.user_id IS NOT NULL THEN TRUE ELSE FALSE END AS completed FROM questions q LEFT JOIN userQuestions uq ON q.question_id = uq.question_id AND uq.user_id = '{id}' WHERE (uq.user_id = '{id}' OR uq.user_id IS NULL) AND q.topic_name ='{topic}' order by q.question_name"
        queryRes = self.dbObj.selectQuery(query, False)
        #print(queryRes)
        easyArr, mediumArr, hardArr = [], [], [] 
        for data in queryRes:
            question_url, question_id, topic_name, question_name, level, platform, completed = data[0], data[1], data[2], data[3], data[4], data[5], data[6]
            if level == "easy":
                formattedData = {"completed": completed == 1, "id": question_id, "name": question_name, "platform": platform, "url": question_url}
                easyArr.append(formattedData)
            elif level == "medium":
                formattedData = {"completed": completed == 1, "id": question_id, "name": question_name, "platform": platform, "url": question_url}
                mediumArr.append(formattedData)
            elif level == "hard":
                formattedData = {"completed": completed == 1, "id": question_id, "name": question_name, "platform": platform, "url": question_url}
                hardArr.append(formattedData)
        easyA = {"body": easyArr, "cardTitle": "Easy", "cardType": "easy"}
        mediumA = {"body": mediumArr, "cardTitle": "Medium", "cardType": "medium"}
        hardA = {"body": hardArr, "cardTitle": "Hard", "cardType": "hard"}
        selectedTopicData1 = [easyA, mediumA, hardA]
        return selectedTopicData1
