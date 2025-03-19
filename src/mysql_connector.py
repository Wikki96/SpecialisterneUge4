import mysql.connector

class MySQLConnector:
    def __init__(self, user, password, database):
        try:
            self.con = mysql.connector.connect(
                host="localhost", user=user, 
                password=password, database=database)
        except ConnectionError:
            print("Could not connect to database")
            raise
        self.cursor = self.con.cursor()

    def get_con(self):
        return self.con

    def execute(self, query):
        self.cursor.execute(query)
        return
    
    def commit(self):
        self.con.commit()
        return
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    