import mysql_connector
import os
from crud_operations import CRUD
from load_config import load_config
from src.combined_crud import CombinedCrud
from src.split_crud import SplitCrud

def populate_table(filename, table, crud: CRUD):
    """Fill the table with the values in the csv file"""
    with open(os.path.join("Data", filename), "r") as f:
            columns = f.readline()
            while True:
                line = f.readline()
                if line == "":
                    break
                crud.insert_row(line, table)
    return

if __name__ == "__main__":
    config = load_config()
    combined_connector = mysql_connector.MySQLConnector()
    combined_crud = CRUD(CombinedCrud(combined_connector))
    combined_crud.create_database(config["database1"])
    combined_crud.create_table(
        "orders_combined",
        """(id INTEGER NOT NULL,
            `date_time` DATETIME,
            `customer_name` VARCHAR(30),
            `customer_email` VARCHAR(50),
            `product_name` VARCHAR(20),
            `product_price` FLOAT,
            CONSTRAINT `PK_orders_combined` PRIMARY KEY (`id`))
         """
    )
    populate_table("orders_combined.csv", "orders_combined", 
                   combined_crud)
    split_connector = mysql_connector.MySQLConnector()
    split_crud = CRUD(SplitCrud(split_connector))
    split_crud.create_database(config["database2"])
    split_crud.create_table(
        "customers",
        """(customer_id INTEGER NOT NULL,
            `customer_name` VARCHAR(30),
            `customer_email` VARCHAR(50),
            CONSTRAINT `PK_customers` PRIMARY KEY (`customer_id`))
        """
    )
    populate_table("customers.csv", "customers", split_crud)
    split_crud.create_table(
         "products",
         """(product_id INTEGER NOT NULL,
            `product_name` VARCHAR(20),
            `product_price` FLOAT,
            CONSTRAINT `PK_products` PRIMARY KEY (`product_id`))
         """
    )
    populate_table("products.csv", "products", split_crud)
    split_crud.create_table(
         "orders",
         """(id INTEGER NOT NULL,
            `date_time` DATETIME,
            `customer_id` INTEGER NOT NULL,
            `product_id` INTEGER NOT NULL,
            CONSTRAINT `PK_orders` PRIMARY KEY (`id`),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id));
         """
    )
    populate_table("orders.csv", "orders", split_crud)




