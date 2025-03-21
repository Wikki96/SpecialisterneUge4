from src.mysql_connector import MySQLConnector

class CrudMode:
    """Interface for dependency injection into crud_operations"""

    mysql_connector: MySQLConnector

    def set_tables_all():
        pass
    
    def update_product_bought():
        pass
    