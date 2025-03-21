from src.crud_mode import CrudMode


class BaseCrud(CrudMode):
    def select(self, select_statement):
        """Execute the selection and return a list with the data."""
        return self.__execute(select_statement)
    
    def update(self, column, new_value, condition_column, 
               condition_value, comparator="="):
        """Update the values in column to new_value if it 
        fulfills the condition.
        """
        update = f"""UPDATE {self.table} SET {column} = '{new_value}' 
                 WHERE {condition_column} {comparator} '{condition_value}'"""
        self.__execute(update)
        return

    def __execute(self, query):
        return self.mysql_connector.execute(query)