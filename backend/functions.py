import random
import json
import requests
from datetime import date
from geopy import distance

def execute_sql(connection, sql):
    # print(f"execute: [{sql}]")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor.close()
    return values

def get_airports(connection):
    sql = """SELECT iso_country, ident, name, type, latitude_deg, longitude_deg
             FROM airport"""
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_airports_player(connection, player):
    sql = "select iso_country, ident, name, type, latitude_deg, longitude_deg from airport where iso_country not in (select country from country_visited where player=" + str(player) + ")"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# get all goals
def get_goals(connection):
    sql = f'''SELECT * FROM goal'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# check if airport has a goal
def check_goal(connection, g_id, cur_airport):
    sql = f'''SELECT ports.id, goal, goal.id as goal_id, name, money
    FROM ports
    JOIN goal ON goal.id = ports.goal
    WHERE player = %s
    AND airport = %s'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (g_id, cur_airport))
    result = cursor.fetchone()
    if result is None:
        return 0
    return result["money"]

def create_game(connection, p_name, cur_airport, start_money, a_ports, profession):
    sql = f'''INSERT INTO player (p_name, location, currency) VALUES (%s, %s, %s)'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (p_name, cur_airport, start_money))
    g_id = cursor.lastrowid


    goals = get_goals(connection)
    goal_list = []
    for goal in goals:
        for i in range(0, goal['probability'], 1):
            goal_list.append(goal['id'])
    #print(goal_list)

    g_ports = a_ports[1:].copy()
    random.shuffle(g_ports)

    for i, goal_id in enumerate(goal_list):
        sql = "INSERT INTO ports (player, airport, goal) VALUES (%s, %s, %s);"
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, (g_id, g_ports[i]['ident'], goal_id))

    return g_id

def get_airport_info(connection, icao):
    sql = f'''SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result

def checkMoonPhase():
    response = requests.get("https://users.metropolia.fi/~royk/fullmoon.json")
    if response.status_code == 200:
        y = str(date.today().strftime("%Y"))
        m = str(date.today().strftime("%m"))
        d = str(date.today().strftime("%d"))

        fullmoon_ym = response.json()["fullmoon"][y][m]
        if (len(fullmoon_ym) == 1 and fullmoon_ym[0] == d):
            return 10000
        elif (len(fullmoon_ym) > 1):
            for x in fullmoon_ym:
                if x == d:
                    return 10000
    return 0

def visited_country(connection, country, player_id):
    sql = "INSERT INTO country_visited (player, country) VALUES (%s, %s)"
    cursor = connection.cursor()
    cursor.execute(sql, (player_id, country))
    connection.commit()
    cursor.close()

def calculateFlyCost(connection, current, target, multiplier = 1):
    start = get_airport_info(connection, current)
    end = get_airport_info(connection, target)
    return int(multiplier * distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km)

#def player_getLocation(connection, player):
#    sql = "select ident, airport.name as 'airport_name', country.name as 'country_name', country.iso_country from airport, country where airport.iso_country=country.iso_country and ident='" + player.location + "'";
#    return execute_sql(connection, sql)[0]
