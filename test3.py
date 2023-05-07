from regression import get_coefficients, home_stats_list, away_stats_list, stats_list
from db import get_value
import math
import numpy as np
from collections import Counter


Time = "19:00"
HomeTeam = "Arsenal"
AwayTeam = "Aston Villa"
League = "Premier League"
Country = "ENG"
todays_date = "2023-02-28"

result = get_coefficients(str(League), str(Country))

home_coeff = result[0]
away_coeff = result[1]
###########################ALL DATA#################################################
league_stats = {}
home_stats = {}
away_stats = {}



for stat in stats_list:
    #Goals scoerd
    home_avr = f"SELECT AVG({stat}) FROM Games WHERE HomeTeam = '{HomeTeam}' AND League = '{League}' AND {stat} IS NOT NULL"
    home_avr = get_value(home_avr,)
    home_avr = round(home_avr, 2)
    
    home_stats[stat] = home_avr

    

for stat in stats_list:
#Goals scoerd
    away_avr = f"SELECT AVG({stat}) FROM Games WHERE AwayTeam = '{AwayTeam}' AND League = '{League}' AND {stat} IS NOT NULL"
    away_avr = get_value(away_avr,)
    away_avr = round(away_avr, 2)
    
    away_stats[stat] = away_avr

    

for stat in stats_list:
#Goals scoerd
    league_avr = f"SELECT AVG({stat}) FROM Games WHERE League = '{League}' AND {stat} IS NOT NULL"
    league_avr = get_value(league_avr,)
    league_avr = round(league_avr, 2)
    
    league_stats[stat] = league_avr

    

Home_xStats = {}
Away_xStats = {}

for stat in home_stats_list:
    
    home_att_str = home_stats[stat] / league_stats[stat]
    away_def_str = away_stats[stat] / league_stats[stat]
    league_avr = league_stats[stat]
    xStat = home_att_str * away_def_str * league_avr

    xstat = round(home_att_str * away_def_str * league_avr ,2)
    Home_xStats[stat] = xstat

    
    

for stat in away_stats_list:
    
    away_att_str = away_stats[stat] / league_stats[stat]
    home_def_str = home_stats[stat] / league_stats[stat]
    league_avr = league_stats[stat]
    xStat = home_att_str * away_def_str * league_avr

    xstat = round(away_att_str * home_def_str * league_avr ,2)
    Away_xStats[stat] = xstat

    
    


xStats = {**Home_xStats, **Away_xStats}



Home_xG = result[2]
Away_xG = result[3]




for stat in stats_list:
    try:
        xg = home_coeff[stat] * xStats[stat]
        Home_xG = Home_xG + xg
    except:
        pass
    

for stat in stats_list:
    try:
        xg = away_coeff[stat] * xStats[stat]
        Away_xG = Away_xG + xg
    except:
        pass

#######################################################################################

try: 
    limit = 10

    ##########################LATEST GAMES#################################################
    league_stats = {}
    latest_home_stats = {}
    latest_away_stats = {}



    for stat in stats_list:
    #Goals scoerd
        latest_home_avr = f"""
                    SELECT AVG({stat}) 
                    FROM (
                        SELECT {stat}
                        FROM Games 
                        WHERE HomeTeam = '{HomeTeam}' AND League = '{League}' AND {stat} IS NOT NULL
                        ORDER BY date DESC
                        LIMIT {limit}
                    ) AS recent_games;
                """
        latest_home_avr = get_value(latest_home_avr,)
        latest_home_avr = round(latest_home_avr, 2)

        latest_home_stats[stat] = latest_home_avr



    for stat in stats_list:
    #Goals scoerd
        latest_away_avr = f"""
                    SELECT AVG({stat}) 
                    FROM (
                        SELECT {stat}
                        FROM Games 
                        WHERE AwayTeam = '{AwayTeam}' AND League = '{League}' AND {stat} IS NOT NULL
                        ORDER BY date DESC
                        LIMIT {limit}
                    ) AS recent_games;
                """
        latest_away_avr = get_value(latest_away_avr,)
        latest_away_avr = round(latest_away_avr, 2)

        latest_away_stats[stat] = latest_away_avr

    for stat in stats_list:
    #Goals scoerd
        league_avr = f"SELECT AVG({stat}) FROM Games WHERE League = '{League}' AND {stat} IS NOT NULL"
        league_avr = get_value(league_avr,)
        league_avr = round(league_avr, 2)
        
        league_stats[stat] = league_avr




    latest_Home_xStats = {}
    latest_Away_xStats = {}

    for stat in home_stats_list:

        latest_home_att_str = latest_home_stats[stat] / league_stats[stat]
        latest_away_def_str = latest_away_stats[stat] / league_stats[stat]
        league_avr = league_stats[stat]
        latest_xStat = latest_home_att_str * latest_away_def_str * league_avr

        latest_xstat = round(latest_home_att_str * latest_away_def_str * league_avr ,2)
        latest_Home_xStats[stat] = latest_xstat




    for stat in away_stats_list:

        latest_away_att_str = latest_away_stats[stat] / league_stats[stat]
        latest_home_def_str = latest_home_stats[stat] / league_stats[stat]
        league_avr = league_stats[stat]
        latest_xStat = latest_home_att_str * latest_away_def_str * league_avr

        latest_xstat = round(latest_away_att_str *latest_home_def_str * league_avr ,2)
        latest_Away_xStats[stat] = latest_xstat





    latest_xStats = {**latest_Home_xStats, **latest_Away_xStats}



    latest_Home_xG = result[2]
    latest_Away_xG = result[3]




    for stat in stats_list:
        try:
            latest_xg = home_coeff[stat] * latest_xStats[stat]
            latest_Home_xG = latest_Home_xG + latest_xg
        except:
            pass


    for stat in stats_list:
        try:
            latest_xg = away_coeff[stat] * latest_xStats[stat]
            latest_Away_xG = latest_Away_xG + latest_xg
        except:
            pass
    ################################################################################ 
except:
    pass


try:
    new_Home_xG = math.sqrt(Home_xG * latest_Home_xG)
    new_Away_xG = math.sqrt(Away_xG * latest_Away_xG)
except:
    new_Home_xG = Home_xG
    new_Away_xG = Away_xG




n_simulations = 10000
home_wins = 0
away_wins = 0
draws = 0
over_2_5 = 0
btts = 0
scores = []

for i in range(n_simulations):
    # Simulate the number of goals each team scores
    home_goals = np.random.poisson(new_Home_xG)
    away_goals = np.random.poisson(new_Away_xG)
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


# Calculate the percentage chance of each outcome

home_win_pct = home_wins / n_simulations * 100
away_win_pct = away_wins / n_simulations * 100
draw_pct = draws / n_simulations * 100



over_2_5_pct = over_2_5 / n_simulations * 100
under_2_5_pct = (n_simulations - over_2_5) / n_simulations * 100



btts_pct = btts / n_simulations * 100
no_btts_pct = (n_simulations - btts) / n_simulations * 100



home_odds = round((1 / home_win_pct) * 100,2)
draw_odds = round((1 / draw_pct) * 100,2)
away_odds = round((1 / away_win_pct) * 100,2)



over_2_5_odds = round((1 / over_2_5_pct) * 100,2)
under_2_5_odds = round((1 / under_2_5_pct) * 100,2)



btts_odds = round((1 / btts_pct) * 100,2)
no_btts_odds = round((1 / no_btts_pct) * 100,2)



most_result = Counter(scores)
most_common_result = most_result.most_common(1)[0][0]
count = scores.count(most_common_result)

most_common_result_pct = count / n_simulations * 100
most_common_result_odds = round((1 / most_common_result_pct) * 100,2)
    



get_league_games = f"SELECT COUNT(id) FROM Games WHERE League = '{League}' AND Country = '{Country}'"
count = get_value(get_league_games)


print("----------")
print(League,"|",Country,"(",count,")")
print(Time,"|", todays_date)

print(HomeTeam, home_odds,"(",round(home_win_pct,2),"% )")
print("Draw", draw_odds,"(",round(draw_pct,2),"% )")
print(AwayTeam, away_odds,"(",round(away_win_pct,2),"% )")



print("Over 2.5 goals:",over_2_5_odds,"(",round(over_2_5_pct,2),"% )")
print("Under 2.5 goals:",under_2_5_odds,"(",round(under_2_5_pct,2),"% )")



print("BTTS:",btts_odds,"(",round(btts_pct,2),"% )")
print("NOT BTTS:",no_btts_odds,"(",round(no_btts_pct,2),"% )")



print("Most common result:", most_common_result, most_common_result_odds,"(",round(most_common_result_pct,2),"% )" )