import sqlite3

def call_db(query: str):
        conn = sqlite3.connect("MatchDB.db")
        cur = conn.cursor()
        res = cur.execute(query)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data

def get_value(query: str, *args):
    conn = sqlite3.connect("MatchDB.db")
    cur = conn.cursor()
    cur.execute(query, args)
    res = cur.fetchone()
    value = res[0]
    cur.close()
    conn.close()
    return value

query = """
    CREATE TABLE IF NOT EXISTS Games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id int,
        date DATE,
        League VARXHAR(255),
        Country VARCHAR(255),
        HomeTeam VARCHAR(255),
        AwayTeam VARCHAR(255),
        HGoals int,
        AGoals int,
        HomexG float,
        AwayxG float,
        HomePoss int,
        AwayPoss int,
        HomeShots int,
        AwayShots int,
        HomeSonT int,
        AwaySonT int,
        HomeSoffT int,
        AwaySoffT int,
        HomeBS int,
        AwayBS int,
        HomeCor int,
        AwayCor int,
        HomeOff int,
        AwayOff int,
        HomeFoul int,
        AwayFoul int,
        HomeYellow int,
        AwayYellow int,
        HomeRed int,
        AwayRed int,
        HomePass int,
        AwayPass int,
        HomeAccPass int,
        AwayAccPass int,
        HomePassOff int,
        AwayPassOff int,
        HomeAccLongB int,
        AwayAccLongB int,
        HomeAccLongBpercent int,
        AwayAccLongBpercent int,
        HomeAccCross int,
        AwayAccCross int,
        HomeAccCrosspercent int,
        AwayAccCrosspercent int,
        HomeSuccDribb int,
        AwaySuccDribb int,
        HomeSuccDribbpercent int,
        AwaySuccDribbpercent int,
        HomeDuelsW int,
        AwayDuelsW int,
        HomeTackW int,
        AwayTackW int,
        HomeTackWpercent int,
        AwayTackWpercent int,
        HomeInt int,
        AwayInt int,
        HomeClear int,
        AwayClear int
    )
"""

call_db(query)

query = """
    CREATE TABLE IF NOT EXISTS Leagues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        League VARCHAR(255),
        Nation VARCHAR(255)
    )
"""
call_db(query)


query = """
    CREATE TABLE IF NOT EXISTS Teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Team VARCHAR(255)
    )
"""
call_db(query)

query = """
    CREATE TABLE IF NOT EXISTS Players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INT,
        date DATE,
        player_id INT,
        HA VARCHAR(255),
        status VARCHAR(255),
        name VARCHAR(255),
        position VARCHAR(255),
        role VARCHAR(255),
        total_min INT,
        goals INT,
        assists INT,
        goals_for INT,
        goals_against INT
    )
"""
call_db(query)
