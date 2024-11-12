import mysql.connector
import os
from urllib.parse import urlparse

class DatabaseConnector:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        url = os.getenv('CLEARDB_DATABASE_URL')
        if url is None:
            raise Exception("CLEARDB_DATABASE_URL environment variable not set.")

        url = urlparse(url)
        return mysql.connector.connect(
            host=url.hostname,
            user=url.username,
            password=url.password,
            database=url.path[1:]
        )

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
