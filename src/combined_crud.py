from src.base_crud import BaseCrud
from src.mysql_connector import MySQLConnector

class CombinedCrud(BaseCrud):

    table = "orders_combined"

    def __init__(self, mysql_connector: MySQLConnector):
        """Sets the connection object. 
        Requires a MySQLConnector class as input.
        """
        self.mysql_connector: MySQLConnector = mysql_connector

    def set_tables_all(self):
        return self.table 

    def update_product_bought(self, order_id, product_name):
        
        select = f"""SELECT product_price FROM {self.table} 
                 WHERE product_name = '{product_name}' LIMIT 1"""
        product_price, = self.select(select)
        self.update("product_name", product_name, 
                    "id", order_id)
        self.update("product_price", product_price[0], "id", order_id)
        return
    
    def select_order_by_customer(self, customer_name):
        select = f"""SELECT id FROM {self.table} 
                 WHERE customer_name = '{customer_name}'"""
        return self.select(select)