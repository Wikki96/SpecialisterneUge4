import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.mysql_connector import MySQLConnector

if __name__ == "__main__":
    connection_info = ["root", "250303", "primer"]
    connector = MySQLConnector(*connection_info)
    connector.create("100,2025-03-14T15:24:45+01:00,Wendy Lockman,wendy.lockman@yahoo.com,Headphones,339.31143")

    data = connector.read(("id", "customer_name"), "id = '100'")
    print(data)
    connector.update("customer_name = 'Johm Smith'", "id = '100'")
    data = connector.read(("id", "customer_name"), "id = '100'")
    connector.delete("id = '100'")
    print(data)