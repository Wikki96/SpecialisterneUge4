import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.mysql_connector import MySQLConnector

class CRUD:
    """Handles basic queries for the table orders_combined.
    Public methods:
    insert_row
    select_columns
    select_name_by_id
    update
    delete
    create_database
    create_table
    Instance variables:
    mysql_connector - an instance of the MySQLConnector class
    table - the current table being worked on
    """
    def __init__(self, mysql_connector: MySQLConnector):
        """Sets the connection object. 
        Requires a MySQLConnector class as input.
        """
        self.mysql_connector = mysql_connector
        self.table = "dummy"

    def select_tables(self, *tables, relations=[]):
        table = tables[0]
        for i, (column1, column2) in enumerate(relations):
            table = table + " INNER JOIN " + tables[i+1] \
                + " ON " + tables[0] + "." + column1 + " = " \
                + tables[i+1] + "." + column2 
        self.table = table
        return

    def insert_row(self, row):
        """Insert row into table"""
        row = row.split(",")
        row = ["'" + entry + "'" for entry in row]
        insert = "INSERT INTO " + self.table + " VALUES " \
                 + "(" + ", ".join(row) + ")" 
        self.__execute(insert)
        self.mysql_connector.commit()
        return

    def select_columns(self, columns):
        select = "SELECT " + ", ".join(columns) \
               + " FROM " + self.table
        self.__execute(select)
        data = self.mysql_connector.fetchall()
        return data
    
    def select_name_by_id(self, id):
        select = "SELECT id, customer_name FROM " + self.table + \
                 " WHERE id = '" + id + "'"
        self.__execute(select)
        data = self.mysql_connector.fetchall()
        return data

    def update(self, what, where):
        update = "UPDATE " + self.table + " SET " \
               + what + " WHERE " + where
        self.__execute(update)
        self.mysql_connector.commit()
        return
    
    def delete(self, where, table=""):
        delete = "DELETE " + table + " FROM " \
            + self.table + " WHERE " + where
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
        """Create table as specified"""
        self.mysql_connector.execute("DROP TABLE IF EXISTS " 
                                     + tablename)
        query = "CREATE TABLE " + tablename + " " + tablestructure
        self.mysql_connector.execute(query)


    def __execute(self, query):
        self.mysql_connector.execute(query)