import mysql.connector
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.load_config import load_config

class MySQLConnector:
    """A wrapper for the mysql connector creating a cursor and 
    handling queries with one method.
    Public methods:
    execute
    """
    def __init__(self, database=""):
        config = load_config()
        self.con = mysql.connector.connect(
            host=config["host"], user=config["user"], 
            password=config["pw"], database=database)
        self.cursor = self.con.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.con.commit()
        return data

    
    