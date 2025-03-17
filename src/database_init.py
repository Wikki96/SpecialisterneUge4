import mysql_connector
import os

if __name__ == "__main__":
    connection_info = ["root", "250303", ""]
    connector = mysql_connector.MySQLConnector(*connection_info)

    connector.execute_query("DROP DATABASE IF EXISTS primer")
    connector.execute_query("CREATE DATABASE IF NOT EXISTS primer")
    connector.execute_query("USE primer")

    with open(os.path.join("Data", "orders_combined.csv"), "r") as f:
        columns = f.readline()
        connector.execute_query("DROP TABLE IF EXISTS `orders_combined`")
        query = """CREATE TABLE `orders_combined` (
                id INTEGER NOT NULL,
                `date_time` DATETIME,
                `customer_name` VARCHAR(30),
                `customer_email` VARCHAR(50),
                `product_name` VARCHAR(20),
                `product_price` FLOAT,
                CONSTRAINT `PK_orders_combined` PRIMARY KEY (`id`));"""
        connector.execute_query(query)
        while True:
            line = f.readline()
            if line == "":
                break
            line = line.split(",")
            line = ["'" + entry + "'" for entry in line]
            insert = "INSERT INTO orders_combined (" + columns + ") VALUES (" + ", ".join(line) + ")"
            connector.execute_query(insert)
        connector.commit()
                 


