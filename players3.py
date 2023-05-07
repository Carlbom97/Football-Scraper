import requests
import json
from db import *
from collections import Counter
import numpy as np

def get_starter_stats(id):

    

    match_url = "https://www.fotmob.com/api/matchDetails?matchId=" + str(id)

    res = requests.get(match_url)
    jasondata = res.json()

    League = jasondata['general']['parentLeagueName']
    Country = jasondata['general']['countryCode']

    get_leauge_home = f"SELECT AVG(HGoals) FROM Games WHERE League = '{League}' AND Country = '{Country}'"
    get_leauge_away = f"SELECT AVG(AGoals) FROM Games WHERE League = '{League}' AND Country = '{Country}'"
    league_home_avr = get_value(get_leauge_home)
    league_away_avr = get_value(get_leauge_away)

    home_ids = []
    away_ids = []

    for i in range(0,2):
        for j in range(0,12):
            for k in range(0,12):

                try:

                    player_id = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['id']

                    name = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['name']['fullName']

                    if i == 0:
                        home_away = 'home'

                    if i == 1:
                        home_away = 'away'

                    if home_away == 'home':
                        home_ids.append(player_id)

                    if home_away == 'away':
                        away_ids.append(player_id)

                except:
                    pass
    
    home_goals = []
    home_conceded = []
    away_goals = []
    away_conceded = []

    for player in home_ids:
        try:
            minutes_query = f"SELECT SUM(total_min) FROM Players WHERE player_id = {player} AND HA = 'Home'"
            goals_query = f"SELECT SUM(goals_for) FROM Players WHERE player_id = {player} AND HA = 'Home'"
            conceded_query = f"SELECT SUM(goals_against) FROM Players WHERE player_id = {player} AND HA = 'Home'"

            minutes = get_value(minutes_query)
            goals = get_value(goals_query)
            conceded = get_value(conceded_query)
            games = int(minutes) / 90

            home_goals.append(int(goals)/games)
            home_conceded.append(int(conceded)/games)

            try:
                file = open("Player_Stats/" + "string" + ".txt", "w")
                file.write(player)
                file.close()
            except:
                pass

        except:
            pass

    for player in away_ids:
        try:
            minutes_query = f"SELECT SUM(total_min) FROM Players WHERE player_id = {player} AND HA = 'Away'"
            goals_query = f"SELECT SUM(goals_for) FROM Players WHERE player_id = {player} AND HA = 'Away'"
            conceded_query = f"SELECT SUM(goals_against) FROM Players WHERE player_id = {player} AND HA = 'Away'"

            minutes = get_value(minutes_query)
            goals = get_value(goals_query)
            conceded = get_value(conceded_query)
            games = int(minutes) / 90

            away_goals.append(int(goals)/games)
            away_conceded.append(int(conceded)/games)

        except:
            pass


    home_att_str = np.mean(home_goals) / league_home_avr
    home_def_str = np.mean(home_conceded) / league_away_avr
    away_att_str = np.mean(away_goals) / league_away_avr
    away_def_str = np.mean(away_conceded) /league_home_avr

    xG_home = home_att_str * away_def_str * league_home_avr
    xG_away = away_att_str * home_def_str * league_away_avr


    n_simulations = 10000
    home_wins = 0
    away_wins = 0
    draws = 0
    over_2_5 = 0
    btts = 0
    scores = []
    
    for i in range(n_simulations):
        # Simulate the number of goals each team scores
        home_goals = np.random.poisson(xG_home)
        away_goals = np.random.poisson(xG_away)
        score = str(home_goals)+"-"+str(away_goals)
        scores.append(score)

        # Determine the outcome of the match based on the number of goals
        if home_goals > away_goals:
            home_wins += 1
        elif away_goals > home_goals:
            away_wins += 1
        else:
            draws += 1

        if home_goals + away_goals > 2.5:
            over_2_5 += 1

        if home_goals > 0.5 and away_goals > 0.5:
            btts += 1

    home_win_pct = home_wins / n_simulations * 100
    away_win_pct = away_wins / n_simulations * 100
    draw_pct = draws / n_simulations * 100

    home_odds = round((1 / home_win_pct) * 100,2)
    draw_odds = round((1 / draw_pct) * 100,2)
    away_odds = round((1 / away_win_pct) * 100,2)

    over_2_5_pct = over_2_5 / n_simulations * 100
    under_2_5_pct = (n_simulations - over_2_5) / n_simulations * 100
    

    
    btts_pct = btts / n_simulations * 100
    no_btts_pct = (n_simulations - btts) / n_simulations * 100

    over_2_5_odds = round((1 / over_2_5_pct) * 100,2)
    under_2_5_odds = round((1 / under_2_5_pct) * 100,2)
    

    
    btts_odds = round((1 / btts_pct) * 100,2)
    no_btts_odds = round((1 / no_btts_pct) * 100,2)

    most_result = Counter(scores)
    most_common_result = most_result.most_common(1)[0][0]
    count = scores.count(most_common_result)

    most_common_result_pct = count / n_simulations * 100
    most_common_result_odds = round((1 / most_common_result_pct) * 100,2)

    print("Home", home_odds,"(",round(home_win_pct,2),"% )")
    print("Draw", draw_odds,"(",round(draw_pct,2),"% )")
    print("Away", away_odds,"(",round(away_win_pct,2),"% )")
    print("Over", over_2_5_odds,"(",round(over_2_5_pct,2),"% )")
    print("Under", under_2_5_odds,"(",round(under_2_5_pct,2),"% )")
    print("BTTS", btts_odds,"(",round(btts_pct,2),"% )")
    print("No BTTS", no_btts_odds,"(",round(no_btts_pct,2),"% )")
    print("Most common result:", most_common_result, most_common_result_odds,"(",round(most_common_result_pct,2),"% )" )
    



get_starter_stats(3901240)