import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.split_crud import SplitCrud
from src.combined_crud import CombinedCrud
from src.mysql_connector import MySQLConnector
from src.crud_operations import CRUD
from src.load_config import load_config

if __name__ == "__main__":
    """Run this after running database_init.py to test"""
    config = load_config()
    connector = MySQLConnector(config["database1"])
    combined_crud = CRUD(CombinedCrud(connector))
    combined_crud.delete("id", "100")
    combined_crud.insert_row("100,2025-03-14T15:24:45+01:00,Wendy Lockman"
    ",wendy.lockman@yahoo.com,Headphones,339.31143", "orders_combined")
    data = combined_crud.select_product_by_order("100")
    print(data)
    combined_crud.update_product_bought("100", "Mouse")
    data = combined_crud.select_product_by_order("100")
    combined_crud.delete("id", "100")
    print(data)

    connector = MySQLConnector(config["database2"])
    split_crud = CRUD(SplitCrud(connector))
    split_crud.delete("id", "100", table="orders")
    split_crud.insert_row("100,2025-03-14T15:24:45+01:00,23,7", "orders")
    data = split_crud.select_product_by_order("100")
    print(data)
    split_crud.update_product_bought("100", "Mouse")
    data = split_crud.select_product_by_order("100")
    split_crud.delete("id", "100", table="orders")
    print(data)
    