from routes.database.database import Database
from projData.topicData import topicMapping

class ProfileDb:
    
    def __init__(self, connection):
        self.dbObj = Database(connection)

    def getUserStatus(self, id):
        query = f"SELECT q.level, COUNT(*) AS level_count, COUNT(DISTINCT uq.question_id) FROM questions q LEFT JOIN userquestions uq ON q.question_id = uq.question_id WHERE uq.user_id = '{id}' or uq.user_id IS NULL GROUP BY q.level"
        queryRes = self.dbObj.selectQuery(query, False)
        query1 = f"SELECT count(q.question_id), count(uq.userquestions_id) FROM questions q LEFT JOIN userquestions uq ON q.question_id = uq.question_id"
        queryRes1 = self.dbObj.selectQuery(query1, False)
        total, totalSolved = queryRes1[0][0], queryRes1[0][1]
        for data in queryRes:
            if data[0] == "easy":
                easyTotal = data[1]
                easySolved = data[2]
            elif data[0] == "medium":
                mediumTotal = data[1]
                mediumSolved = data[2]
            elif data[0] == "hard":
                hardTotal = data[1]
                hardSolved = data[2]
        user_data1 = {"easySolved": easySolved, "easyTotal": easyTotal, "hardSolved": hardSolved, "hardTotal": hardTotal, "mediumSolved": mediumSolved, "mediumTotal": mediumTotal, "total": total, "totalSolved": totalSolved}
        return user_data1
        

    def getTableData(self, id):
        query = f"SELECT q.topic_name, q.question_name, q.question_url, q.level, q.platform, uq.date, CASE WHEN uq.user_id IS NOT NULL THEN TRUE ELSE FALSE END FROM questions q LEFT JOIN userQuestions uq ON q.question_id = uq.question_id AND uq.user_id = '{id}' WHERE (uq.user_id = '{id}' OR uq.user_id IS NULL)"
        queryRes = self.dbObj.selectQuery(query, False)
        rows = []
        for data in queryRes:
            date, done, level, platform, question, url = data[5], data[6], data[3], data[4], data[1], data[2]
            if data[0] in topicMapping:
                topic = topicMapping[data[0]]
            if done == 1:
                done = "Yes"
            else:
                done = "No"
            formattedData = {"date": date, "done": done, "level": level, "platform": platform, "question": question, "topic": topic, "url": url}
            rows.append(formattedData)
        finalData = {"rows": rows}
        return finalData