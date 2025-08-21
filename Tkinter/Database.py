import mysql.connector

class Connector:
    def __init__(self, host, user):
        self.host = host
        self.user = user

    def create_database(self):
        # Prompting the user for database name and password
        database_name = input("Enter the name of the database to create: ")
        password = input("Enter your MySQL password: ")

        # Establishing connection with MySQL server
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=password
            )
            cursor = connection.cursor()

            # Creating the database
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            print(f"Database '{database_name}' created successfully.")

            # Closing the connection
            cursor.close()
            connection.close()

            return database_name, password  # Return database name and password for further use

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def connect_to_database(self, database_name, password):
        # Establishing connection to the specific database
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=password,
                database=database_name
            )
            print(f"Connected to database '{database_name}' successfully.")
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")


# Example usage:
host = "localhost"
user = "root"

db_connector = Connector(host, user)

# Create a database and get the database name and password from the user
database_name, password = db_connector.create_database()

# Connect to the created database
if database_name and password:
    connection = db_connector.connect_to_database(database_name, password)
