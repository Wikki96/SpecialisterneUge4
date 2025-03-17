
class CRUD:
    def __init__(self, mysql_connector):
        self.mysql_connector = mysql_connector

    def insert_row(self, row):
        row = row.split(",")
        row = ["'" + entry + "'" for entry in row]
        insert = "INSERT INTO orders_combined VALUES " \
                 + "(" + ", ".join(row) + ")" 
        self.__execute(insert)
        self.mysql_connector.commit()
        return
    
    def select_columns(self, columns):
        select = "SELECT " + ", ".join(columns) + " FROM orders_combined"
        self.__execute(select)
        data = self.mysql_connector.fetchall()
        return data
    
    def select_name_by_id(self, id):
        select = "SELECT id, customer_name FROM orders_combined " \
                "WHERE id = '" + id + "'"
        self.__execute(select)
        data = self.mysql_connector.fetchall()
        return data

    def update(self, what, where):
        update = "UPDATE orders_combined SET " + what + " WHERE " + where
        self.__execute(update)
        self.mysql_connector.commit()
        return
    
    def delete(self, where):
        delete = "DELETE FROM orders_combined WHERE " + where
        self.__execute(delete)
        self.mysql_connector.commit()
        return
    
    def __execute(self, exp):
        self.mysql_connector.execute_query(exp)