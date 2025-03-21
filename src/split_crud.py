from src.base_crud import BaseCrud
from src.mysql_connector import MySQLConnector

class SplitCrud(BaseCrud):

    table: str

    def __init__(self, mysql_connector: MySQLConnector):
        """Sets the connection object. 
        Requires a MySQLConnector class as input.
        """
        self.mysql_connector: MySQLConnector = mysql_connector
        self.table = "dummy"

    def set_tables(self, *tables, relations: list = []):
        """Set the table to use in other methods."""
        table = tables[0]
        for i, (column1, column2) in enumerate(relations):
            table = f"""{table} INNER JOIN {tables[i+1]}  
            ON {tables[0]}.{column1} = {tables[i+1]}.{column2}"""
        self.table = table
        return table

    def set_tables_all(self):
        table = self.set_tables("orders", "products", "customers",
                       relations=[("product_id", "product_id"), 
                        ("customer_id", "customer_id")])
        return table

    def __select_product_id(self, product_name):
        select = f"""SELECT product_id FROM products 
                 WHERE product_name = '{product_name}'"""
        return self.execute(select)

    def update_product_bought(self, order_id, product_name):
        self.set_tables_all()
        product_id, = self.__select_product_id(product_name)
        self.set_tables("orders")
        self.update("product_id", product_id[0], "id", order_id,)
        return