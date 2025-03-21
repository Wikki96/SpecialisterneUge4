import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.mysql_connector import MySQLConnector
from src.crud_mode import CrudMode

class CRUD:
    """Handles basic queries for the database in the given connector. 
    All methods work on the table stored. All arguments are given as strings
    unless otherwise specified.
    Public methods:
    insert_row
    select_all
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

    def __init__(self, crud_mode: CrudMode):
        """Sets the connection object and crud mode"""
        self.mysql_connector: MySQLConnector = crud_mode.mysql_connector
        self.crud_mode: CrudMode = crud_mode
        self.table: str = crud_mode.set_tables_all()

    def insert_row(self, row, table):
        """Insert row into the selected table."""
        row = row.split(",")
        row = [f"'{entry}'" for entry in row]
        insert = f"INSERT INTO {table} VALUES ({", ".join(row)})"
        self.__execute(insert)
        return

    def select_all(self):
        """Return the entire table."""
        select = f'SELECT * FROM {self.table}'
        return self.__execute(select)

    def select_columns(self, columns):
        """Return the columns given."""
        select = f"SELECT {", ".join(columns)} FROM {self.table}"
        return self.__execute(select)
    
    def select_order_by_customer(self, customer_name):
        select = f"""SELECT id FROM {self.table} 
                 WHERE customer_name = '{customer_name}'"""
        return self.__execute(select)

    def select_product_by_order(self, id):
        """Return the product matching the given order id."""
        select = f"""SELECT product_name, product_price FROM {self.table}
                 WHERE id = '{id}'"""
        return self.__execute(select)
    
    def update_product_bought(self, customer_name, product_name):
        self.crud_mode.update_product_bought(customer_name, product_name)
        return
    
    def delete(self, column, value, table=""):
        """Delete rows where column has value. When using join, table 
        specifies which table to delete from.
        """
        delete = f"""DELETE {table} FROM {self.table} 
                     WHERE {column} = '{value}'"""
        self.__execute(delete)
        return
    
    def create_database(self, name):
        """Create and use the database 'name'."""
        self.mysql_connector.execute(f"DROP DATABASE IF EXISTS {name}")
        self.mysql_connector.execute(f"""CREATE DATABASE 
                                     IF NOT EXISTS {name}""")
        self.mysql_connector.execute(f"USE {name}")
        return 

    def create_table(self, tablename, tablestructure):
        """Create a table as specified."""
        self.mysql_connector.execute(f"""DROP TABLE IF EXISTS 
                                     {tablename}""")
        query = f"CREATE TABLE {tablename} {tablestructure}"
        self.mysql_connector.execute(query)

    def __execute(self, query):
        return self.mysql_connector.execute(query)