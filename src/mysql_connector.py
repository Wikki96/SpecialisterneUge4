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
    
    def __commit(self):
        self.con.commit()
        return
    
    def create(self, row):
        row = row.split(",")
        row = ["'" + entry + "'" for entry in row]
        insert = "INSERT INTO orders_combined VALUES " \
                 + "(" + ", ".join(row) + ")" 
        self.execute_query(insert)
        self.__commit()
        return
    
    def read(self, columns, where=""):
        if where != "":
            where = "WHERE " + where
        select = "SELECT " + ", ".join(columns) + " FROM orders_combined " \
                    + where
        self.execute_query(select)
        data = self.cursor.fetchall()
        return data
    
    def update(self, what, where):
        update = "UPDATE orders_combined SET " + what + " WHERE " + where
        self.execute_query(update)
        self.__commit()
        return
    
    def delete(self, where):
        delete = "DELETE FROM orders_combined WHERE " + where
        self.execute_query(delete)
        self.__commit()
        return