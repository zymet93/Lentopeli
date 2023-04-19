import random

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

# get all goals
def get_goals(connection):
    sql = f'''SELECT * FROM goal'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

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
