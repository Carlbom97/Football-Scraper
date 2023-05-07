from db import call_db, get_value

delete_dublicate = """
    DELETE FROM Games
    WHERE id NOT IN (
    SELECT MIN(id)
    FROM Games
    GROUP BY match_id, date, League, Country, HomeTeam, AwayTeam, HGoals, AGoals, HomexG, AwayxG, HomePoss, AwayPoss, HomeShots, AwayShots, HomeSonT, AwaySonT, HomeSoffT, AwaySoffT, HomeBS, AwayBS, HomeCor, AwayCor, HomeOff, AwayOff, HomeFoul, AwayFoul, HomeYellow, AwayYellow, HomeRed, AwayRed, HomePass, AwayPass, HomeAccPass, AwayAccPass, HomePassOff, AwayPassOff, HomeAccLongB, AwayAccLongB, HomeAccLongBpercent, AwayAccLongBpercent, HomeAccCross, AwayAccCross, HomeAccCrosspercent, AwayAccCrosspercent, HomeSuccDribb, AwaySuccDribb, HomeSuccDribbpercent, AwaySuccDribbpercent, HomeDuelsW, AwayDuelsW, HomeTackW, AwayTackW, HomeTackWpercent, AwayTackWpercent, HomeInt, AwayInt, HomeClear, AwayClear
);
"""

delete_dublicate2 = """
    DELETE FROM Players
    WHERE id NOT IN (
    SELECT MIN(id)
    FROM Games
    GROUP BY match_id, date, player_id, HA, status, name, position, role, total_min, goals, assists, goals_for, goals_against
);
"""

call_db(delete_dublicate2)

# call_db(delete_dublicate)

# delete_teams = """
#     DROP TABLE Teams
# """

# team = "Arsenal"

# get_avr_goals = f"SELECT AVG(HGoals) FROM Games WHERE HomeTeam = '{team}'"

# avr_goals = get_value(get_avr_goals)
# rounded_value = round(avr_goals, 2)
# print(rounded_value)

# season_query = "SELECT "

# query = f"""
#         DROP TABLE players
#         """
# value = call_db(query)
