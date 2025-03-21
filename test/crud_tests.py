import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.mysql_connector import MySQLConnector
from src.crud_operations import CRUD
from src.load_config import load_config

if __name__ == "__main__":
    """Run this after running database_init.py to test"""
    config = load_config()
    connector = MySQLConnector(config["database1"])
    crud = CRUD(connector)
    crud.set_tables("orders_combined")
    crud.delete("id", "100")
    crud.insert_row("100,2025-03-14T15:24:45+01:00,"
    "Wendy Lockman,wendy.lockman@yahoo.com,Headphones,339.31143")
    data = crud.select_product_by_order("100")
    print(data)
    crud.update("product_name", "Mouse", "id", "100")
    data = crud.select_product_by_order("100")
    crud.delete("id", "100")
    print(data)

    connector = MySQLConnector(config["database2"])
    crud = CRUD(connector)
    relations = [("product_id", "product_id"), 
                 ("customer_id", "customer_id")]
    crud.set_tables("orders", "products", "customers",
                       relations=relations)
    crud.set_tables("orders")
    crud.delete("id", "100")
    crud.insert_row("100,2025-03-14T15:24:45+01:00,0,6")
    crud.set_tables("orders", "products", "customers",
                    relations=relations)
    data = crud.select_product_by_order("100")
    print(data)
    crud.set_tables("orders")
    crud.update("product_id", "3", "id", "100")
    crud.set_tables("orders", "products", "customers",
                    relations=relations)
    data = crud.select_product_by_order("100")
    crud.delete("id", "100", table="orders")
    print(data)
    