import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

class dbConn:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = os.getenv("FG_DB_HOST"),
            port = os.getenv("FG_DB_PORT"),
            database = os.getenv("FG_DB_NAME"),
            user = os.getenv("FG_DB_USER"),
            password = os.getenv("FG_DB_PASS"),
            autocommit = True
        )

    def get_conn(self):
        return self.conn
