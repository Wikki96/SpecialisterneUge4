import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.mysql_connector import MySQLConnector

if __name__ == "__main__":
    connection_info = ["root", "250303", "primer"]
    connector = MySQLConnector(*connection_info)

    data = connector.read('*')
    print(data)