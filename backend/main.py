from flask import Flask, jsonify, render_template, url_for, redirect
from Player import Player
from flask_cors import CORS
from flask import request
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
    if profession == "Construction" or profession == "Coding" or profession == "Driving":
        start_money = 1000
        start_airport = "EFHK"
        playerTimeMax = 24
        all_airports = get_airports(connection)

        start_money = start_money + checkMoonPhase()

        players.append(Player(create_game(connection, player, start_airport, start_money, all_airports, profession), start_airport, playerTimeMax, start_money, all_airports, profession, player, playerTimeMax))
        playersIndex = len(players)-1

        visited_country(connection, get_airport_info(connection, start_airport)["iso_country"], players[playersIndex].id)

        return {
            "playersIndex": playersIndex,
            "playerID": players[playersIndex].id,
            "playerName": players[playersIndex].name,
            "playerTime": players[playersIndex].time,
            "playerTimeMax": players[playersIndex].timeMax,
            "playerMoney": players[playersIndex].money,
            "playerLocation": players[playersIndex].location,
            "playerGoal": players[playersIndex].goal,
            "playerProfession": players[playersIndex].profession,
            "playerCanShuffleWork": players[playersIndex].canShuffleWork,
            "playerCanWorkAmount": players[playersIndex].canWorkAmt
            }
    else: return "failure"

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
        "playerTimeMax": players[playeridx].timeMax,
        "playerMoney": players[playeridx].money,
        "playerLocation": players[playeridx].location,
        "playerGoal": players[playeridx].goal,
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

@app.route('/airports/<playeridx>')
def airportsvisitable(playeridx):
    playeridx = int(playeridx)
    print(playeridx)
    player = players[playeridx]
    airports = get_airports_player(connection, player.id)
    cost_multiplier = 1.5  # adjust this as needed

    for airport in airports:
        airport_id = airport['ident']
        fly_cost = calculateFlyCost(connection, player.location, airport_id, cost_multiplier)
        airport['cost'] = fly_cost


    response = jsonify(airports)
    print(response)
    return response


@app.route('/fly/<playeridx>/<airport>')
def flyto(playeridx, airport):
    playeridx = int(playeridx)

    go = 0
    for x in get_airports_player(connection, players[playeridx].id):
        if airport == x["ident"]:
            go = 1

    cost = calculateFlyCost(connection, players[playeridx].location, airport)
    if (players[playeridx].time > 0 and players[playeridx].money >= cost and go == 1):
        players[playeridx].location = airport
        players[playeridx].money -= cost
        players[playeridx].time -= 1

        players[playeridx].resetWork()
        visited_country(connection, get_airport_info(connection, airport)["iso_country"], players[playeridx].id)
        players[playeridx].money += players[playeridx].setGoal(connection)
        if players[playeridx].money < 0: players[playeridx].money = 0
        return "success"
    return "failure"

@app.route('/work/<playeridx>/<job>')
def work(playeridx, job):
    playeridx = int(playeridx)
    if (players[playeridx].time > 0):

        salary = 0
        rakentajapalkka = 1000
        kuskipalkka = 1200
        koodaripalkka = 1500

        if job == "Construction":
            salary = rakentajapalkka + rakentajapalkka * (2*(job == players[playeridx].profession)) - rakentajapalkka * (0.25*(players[playeridx].profession == "Coding"))
        if job == "Driving":
            salary = kuskipalkka + kuskipalkka * (2*(job == players[playeridx].profession)) - kuskipalkka * (0.25*(players[playeridx].profession == "Coding"))
        if job == "Coding":
            salary = koodaripalkka + koodaripalkka * (2*(job == players[playeridx].profession))

        players[playeridx].money += salary
        players[playeridx].time -= 1
        return "success"
    return "failure"


@app.route('/highscore/add/<playeridx>')
def addtohs(playeridx):
    playeridx = int(playeridx)
    sql = 'update player set currency=' + str(players[playeridx].money) + ' where id=' + str(players[playeridx].id)
    execute_sql(connection, sql)

    sql = "insert into highscore (player) values (" + str(players[playeridx].id) + ")"
    execute_sql(connection, sql)
    return "success, probably"

@app.route('/highscore/get')
def geths():
    sql = "select player.p_name, player.currency from player, highscore where player.id = highscore.player order by player.currency desc limit 5"
    return jsonify(execute_sql(connection, sql))


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
