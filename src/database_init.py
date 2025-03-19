import mysql_connector
import os
from crud_operations import CRUD

def populate_table(filename, table):
    with open(os.path.join("Data", filename), "r") as f:
            columns = f.readline()
            while True:
                line = f.readline()
                if line == "":
                    break
                crud.insert_row(line, table)
    return

if __name__ == "__main__":
    connection_info = ["root", "250303", ""]
    database_name = "primer"
    connector = mysql_connector.MySQLConnector(*connection_info)
    crud = CRUD(connector)
    crud.create_database(database_name)
    crud.create_table(
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
    populate_table("orders_combined.csv", "orders_combined")
    crud.create_table(
        "customers",
        """(customer_id INTEGER NOT NULL,
            `customer_name` VARCHAR(30),
            `customer_email` VARCHAR(50),
            CONSTRAINT `PK_customers` PRIMARY KEY (`customer_id`))
        """
    )
    populate_table("customers.csv", "customers")
    crud.create_table(
         "products",
         """(product_id INTEGER NOT NULL,
            `product_name` VARCHAR(20),
            `product_price` FLOAT,
            CONSTRAINT `PK_products` PRIMARY KEY (`product_id`))
         """
    )
    populate_table("products.csv", "products")
    crud.create_table(
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
    populate_table("orders.csv", "orders")


    #with open(os.path.join("Data", "orders.csv"), "r") as f:
    #    columns = f.readline()
    #    connector.execute("DROP TABLE IF EXISTS `orders`")
    #    query = """CREATE TABLE `orders` (
    #            id INTEGER NOT NULL,
    #            `date_time` DATETIME,
    #            `customer_id` INTEGER NOT NULL,
    #            `product_id` INTEGER NOT NULL,
    #            CONSTRAINT `PK_orders` PRIMARY KEY (`id`)
    #            FOREIGN KEY (customer_id) REFERENCES customers(customer_id))
    #            FOREIGN KEY (product_id) REFERENCES products(product_id));"""
    #    connector.execute(query)
    #    while True:
    #        line = f.readline()
    #        if line == "":
    #            break
    #        crud.insert_row(line)
                 


