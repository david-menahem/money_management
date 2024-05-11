import mysql.connector
from mysql.connector import pooling


class MySQLConnection:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection_pool = None

    def connect(self):
        try:
            self.connection_pool = pooling.MySQLConnectionPool(
                pool_name="my_pool",
                pool_size=5,
                pool_reset_session=True,
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Connected to MySQL database")

        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)

    def get_connection(self):
        try:
            return self.connection_pool.get_connection()
        except mysql.connector.Error as e:
            print("Error getting connection:", e)

    def execute_query(self,query):
        connection = None
        cursor = None
        try:
            connection = self.connection_pool.get_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            connection.commit()
            return data
        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

