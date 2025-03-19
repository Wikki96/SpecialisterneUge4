import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.mysql_connector import MySQLConnector
from src.crud_operations import CRUD

if __name__ == "__main__":
    connection_info = ["root", "250303", "combined"]
    connector = MySQLConnector(*connection_info)
    crud = CRUD(connector)
    crud.set_tables("orders_combined")
    crud.delete("id", "100")
    crud.insert_row("100,2025-03-14T15:24:45+01:00,"
    "Wendy Lockman,wendy.lockman@yahoo.com,Headphones,339.31143")
    
    data = crud.select_name_by_id("100")
    print(data)
    crud.update("customer_name = 'Johm Smith'", "id = '100'")
    data = crud.select_name_by_id("100")
    crud.delete("id", "100")
    print(data)
    connection_info = ["root", "250303", "split"]
    connector = MySQLConnector(*connection_info)
    crud = CRUD(connector)
    relations = [("product_id", "product_id"), 
                 ("customer_id", "customer_id")]
    crud.set_tables("orders", "products", "customers"
                       , relations=relations)
    crud.delete("orders.id", "100", table="orders")
    crud.set_tables("orders")
    crud.insert_row("100,2025-03-14T15:24:45+01:00,0,3")
    crud.set_tables("orders", "products", "customers"
                       , relations=relations)
    data = crud.select_name_by_id("100")
    print(data)
    crud.update("customer_name = 'Johm Smith'", "id = '100'")
    data = crud.select_name_by_id("100")
    crud.delete("orders.id", "100", table="orders")
    print(data)
    