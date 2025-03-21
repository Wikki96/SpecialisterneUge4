from src.mysql_connector import MySQLConnector

class CrudMode:
    """Interface for dependency injection into crud_operations"""

    mysql_connector: MySQLConnector

    def set_tables_all():
        pass
    
    def update_product_bought():
        pass
    
    def select_product_by_order():
        pass
    
    def select_order_by_customer():
        pass