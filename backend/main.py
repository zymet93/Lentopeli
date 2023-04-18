import json
from flask import Flask
from geopy import distance
import random

#database and environment variables
from dbConn import *


db = dbConn()
conn = db.get_conn()
app = Flask(__name__)

@app.route("/placeholder")
def placeholder_function():
    return os.getenv("FG_DB_NAME")

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.1", port=3000)
