from flask import Flask, jsonify
from geopy import distance
from Player import Player
from flask_cors import CORS

#database and environment variables
from dbConn import *

db = dbConn()
connection = db.get_conn()

#various functions
from functions import *

app = Flask(__name__)
CORS(app)

players = []

@app.route("/player/create/<player>/<profession>")
def creategame(player, profession):
    #placeholder
    if True:
    #if profession == "Rakentaja" or profession == "Koodaaja" or profession == "Kuski":
        start_money = 10000
        start_airport = "EFHK"
        all_airports = get_airports(connection)

        start_money = start_money + checkmoonphase()

        players.append(Player(create_game(connection, player, start_airport, start_money, all_airports, profession), start_airport, 12, start_money, all_airports, profession, player))
        playersIndex = len(players)-1

        return {
            "playersIndex": playersIndex,
            "playerID": players[playersIndex].id,
            "playerName": players[playersIndex].name,
            "playerTime": players[playersIndex].time,
            "playerMoney": players[playersIndex].money,
            "playerLocation": players[playersIndex].location,
            "playerProfession": players[playersIndex].profession,
            "playerCanShuffleWork": players[playersIndex].canShuffleWork,
            "playerCanWorkAmount": players[playersIndex].canWorkAmt
            }
    else: return "error"

#get player data
@app.route("/player/<playeridx>/get")
def get_player(playeridx):
    #add check for id?
    playeridx = int(playeridx)
    return {
        "playersIndex": playeridx,
        "playerID": players[playeridx].id,
        "playerName": players[playeridx].name,
        "playerTime": players[playeridx].time,
        "playerMoney": players[playeridx].money,
        "playerLocation": players[playeridx].location,
        "playerProfession": players[playeridx].profession,
        "playerCanShuffleWork": players[playeridx].canShuffleWork,
        "playerCanWorkAmount": players[playeridx].canWorkAmt
    }

# Endpoint to return airport data
@app.route('/airports')
def airports():
    db = dbConn()
    conn = db.get_conn()
    cursor = conn.cursor(dictionary=True)
    sql = """SELECT iso_country, ident, name, type, latitude_deg, longitude_deg
             FROM airport"""
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)


