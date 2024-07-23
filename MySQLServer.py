import mysql.connector
from mysql.connector import errorcode


def create_database():
    try:
        # Connect to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mypassword'
        )
        cursor = conn.cursor()

        # Create the database
        try:
            database_name = 'alx_book_store'
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database alx_book_store created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

        # Close the cursor and connection
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


if __name__ == "__main__":
    create_database()
