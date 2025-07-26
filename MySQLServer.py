import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin",
    database="alx_book_store",
    port=3306
)

mysqlcursor = mydb.cursor()

try:
    mysqlcursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    mysqlcursor.execute("CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    mysqlcursor.execute("USE alx_book_store")
except mysql.connector.Error as err:
    print(f"Error: {err}")
else:
    print("Databse 'alx_book_store' created successfully!")
finally:
    mysqlcursor.close()
    mydb.close()
