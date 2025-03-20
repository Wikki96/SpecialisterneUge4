import mysql.connector

class MySQLConnector:
    def __init__(self, host, user, password, database):
        try:
            self.con = mysql.connector.connect(
                host=host, user=user, 
                password=password, database=database)
        except mysql.connector.errors.InterfaceError:
            print("Oh no!")
            raise
        self.cursor = self.con.cursor()

    def get_con(self):
        return self.con

    def execute(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.con.commit()
        return data

    
    