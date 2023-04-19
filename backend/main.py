import json
from flask import Flask
from geopy import distance
from Player import Player

#database and environment variables
from dbConn import *

db = dbConn()
connection = db.get_conn()

#various functions
from functions import *

app = Flask(__name__)
players = []


@app.route("/creategame/<player>/<profession>")
def creategame(player, profession):
    if profession == "Rakentaja" or profession == "Koodaaja" or profession == "Kuski":
        start_money = 10000
        start_airport = "EFHK"
        all_airports = get_airports(connection)

        players.append(Player(create_game(connection, player, start_airport, start_money, all_airports, profession), start_airport, 12, start_money, all_airports, profession, player))
        playersIndex = len(players)-1

        return {
            "playersIndex": playersIndex,
            "playerID": players[playersIndex].id,
            "playerName": players[playersIndex].name,
            "playerLocation": players[playersIndex].location,
            "playerProfession": players[playersIndex].profession
            }
    else: return "error"

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.1", port=3000)
