import os

class CRUD:
    """Handles basic queries for the table orders_combined.
    Public methods:
    insert_row
    select_columns
    select_name_by_id
    update
    delete
    create_database
    Instance variables:
    mysql_connector - an instance of the MySQLConnector class
    """
    def __init__(self, mysql_connector):
        """Sets the connection object. 
        Requires a MySQLConnector class as input.
        """
        self.mysql_connector = mysql_connector

    def insert_row(self, row, table="orders_combined"):
        """Insert row into table"""
        row = row.split(",")
        row = ["'" + entry + "'" for entry in row]
        insert = "INSERT INTO "+ table + " VALUES " \
                 + "(" + ", ".join(row) + ")" 
        self.__execute(insert)
        self.mysql_connector.commit()
        return

    def select_columns(self, columns):
        select = "SELECT " + ", ".join(columns) \
               + " FROM orders_combined"
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
        update = "UPDATE orders_combined SET " \
               + what + " WHERE " + where
        self.__execute(update)
        self.mysql_connector.commit()
        return
    
    def delete(self, where):
        delete = "DELETE FROM orders_combined WHERE " + where
        self.__execute(delete)
        self.mysql_connector.commit()
        return
    
    def create_database(self, name):
        """Create and use the database 'name'"""
        self.mysql_connector.execute("DROP DATABASE IF EXISTS "
                                            + name)
        self.mysql_connector.execute("CREATE DATABASE " \
                                            "IF NOT EXISTS " + name)
        self.mysql_connector.execute("USE " + name)
        return

    def create_table(self, tablename, tablestructure):
        self.mysql_connector.execute("DROP TABLE IF EXISTS " 
                                     + tablename)
        query = "CREATE TABLE " + tablename + " " + tablestructure
        self.mysql_connector.execute(query)


    def __execute(self, query):
        self.mysql_connector.execute(query)