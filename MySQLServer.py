import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="data_center",
    port=8000
)

mysqlcursor = mydb.cursor()

try:
    mysqlcursor.execute("CREATE TABLE alx_book_store ()")
except mysql.connector.Error as err:
    print(f"Error: {err}")
else:
    print("Databse 'alx_book_store' created successfully!")
finally:
    mysqlcursor.close()
    mydb.close()
