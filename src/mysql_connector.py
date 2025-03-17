import mysql.connector

class MySQLConnector:
    con = ""

    def __init__(self, user, password, database):
        self.con = mysql.connector.connect(host="localhost", user=user, password=password, database=database)
        self.cursor = self.con.cursor()

    def get_con(self):
        return self.con

    def execute_query(self, query):
        self.cursor.execute(query)
        return
    
    def __commit__(self):
        self.con.commit()
        return
    
    def create(self, data):
        insert = "INSERT INTO orders_combined VALUES " + data 
        self.execute_query(insert)
        self.__commit__()
        return
    
    def read(self, columns):
        select = "SELECT " + "".join(columns) + "FROM orders_combined"
        self.execute_query(select)
        data = self.cursor.fetchall()
        return data
    
    def update(self, set, where):
        return