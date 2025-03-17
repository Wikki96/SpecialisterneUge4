import mysql.connector

class MySQLConnector:
    con = ""

    def __init__(self, user, password, database):
        print(user, password, database)
        self.con = mysql.connector.connect(host="localhost", user=user, password=password, database=database)
        self.cursor = self.con.cursor()

    def get_con(self):
        return self.con

    def execute_query(self, query):
        self.cursor.execute(query)
        return
    
    def commit(self):
        self.con.commit()
        return