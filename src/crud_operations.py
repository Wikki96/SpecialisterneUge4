import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.mysql_connector import MySQLConnector

class CRUD:
    """Handles basic queries for the database in the given connector. 
    All methods work on the table stored.
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

    def set_tables(self, *tables, relations=[]):
        """Set the table to use in other methods"""
        table = tables[0]
        for i, (column1, column2) in enumerate(relations):
            table = f"""{table} INNER JOIN {tables[i+1]}  
            ON {tables[0]}.{column1} = {tables[i+1]}.{column2}"""
        self.table = table
        return

    def insert_row(self, row):
        """Insert row into the selected table"""
        row = row.split(",")
        row = [f"'{entry}'" for entry in row]
        insert = f"INSERT INTO {self.table} VALUES ({", ".join(row)})"
        self.__execute(insert)
        self.mysql_connector.commit()
        return

    def __select(self, select_statement):
        """Execute the selection"""
        self.__execute(select_statement)
        data = self.mysql_connector.fetchall()
        return data

    def select_all(self):
        """Return the entire table"""
        select = f'SELECT * FROM {self.table}'
        return self.__select(select)

    def select_columns(self, columns):
        """Return the columns given"""
        select = f"SELECT {", ".join(columns)} FROM {self.table}"
        return self.__select(select)
    
    def select_name_by_id(self, id):
        """Return id and name matching the given id"""
        select = f"""SELECT id, customer_name FROM {self.table}
                 WHERE id = '{id}'"""
        return self.__select(select)

    def update(self, what, where):
        """Update the values at where with the information of what"""
        update = f"UPDATE {self.table} SET {what} WHERE {where}"
        self.__execute(update)
        self.mysql_connector.commit()
        return
    
    def delete(self, column, value, table=""):
        """Delete rows where column has value. When using join, table 
        specifies which table to delete from
        """
        delete = f"""DELETE {table} FROM {self.table} 
                     WHERE {column} = '{value}'"""
        self.__execute(delete)
        self.mysql_connector.commit()
        return
    
    def create_database(self, name):
        """Create and use the database 'name'"""
        self.mysql_connector.execute(f"DROP DATABASE IF EXISTS {name}")
        self.mysql_connector.execute(f"""CREATE DATABASE 
                                     IF NOT EXISTS {name}""")
        self.mysql_connector.execute(f"USE {name}")
        return

    def create_table(self, tablename, tablestructure):
        """Create table as specified"""
        self.mysql_connector.execute(f"""DROP TABLE IF EXISTS 
                                     {tablename}""")
        query = f"CREATE TABLE {tablename} {tablestructure}"
        self.mysql_connector.execute(query)


    def __execute(self, query):
        self.mysql_connector.execute(query)