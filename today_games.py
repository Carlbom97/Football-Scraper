import requests
from db import call_db, get_value
import json
import os
from scipy.stats import poisson
import numpy as np
from regression import get_coefficients, stats_list, home_stats_list, away_stats_list
from collections import Counter
import math
import pandas as pd

url_list = [
            "https://www.fotmob.com/api/leagues?id=47",
            "https://www.fotmob.com/api/leagues?id=38",
            "https://www.fotmob.com/api/leagues?id=112",
            "https://www.fotmob.com/api/leagues?id=40",
            "https://www.fotmob.com/api/leagues?id=268",
            "https://www.fotmob.com/api/leagues?id=46",
            "https://www.fotmob.com/api/leagues?id=48",
            "https://www.fotmob.com/api/leagues?id=53",
            "https://www.fotmob.com/api/leagues?id=110",
            "https://www.fotmob.com/api/leagues?id=54",
            "https://www.fotmob.com/api/leagues?id=146",
            "https://www.fotmob.com/api/leagues?id=55",
            "https://www.fotmob.com/api/leagues?id=86",
            "https://www.fotmob.com/api/leagues?id=57",
            "https://www.fotmob.com/api/leagues?id=59",
            "https://www.fotmob.com/api/leagues?id=61",
            "https://www.fotmob.com/api/leagues?id=196",
            "https://www.fotmob.com/api/leagues?id=63",
            "https://www.fotmob.com/api/leagues?id=9080",
            "https://www.fotmob.com/api/leagues?id=67",
            "https://www.fotmob.com/api/leagues?id=168",
            "https://www.fotmob.com/api/leagues?id=69",
            "https://www.fotmob.com/api/leagues?id=71",
            "https://www.fotmob.com/api/leagues?id=130",
            "https://www.fotmob.com/api/leagues?id=87",
            "https://www.fotmob.com/api/leagues?id=10216",
            "https://www.fotmob.com/api/leagues?id=42",
            "https://www.fotmob.com/api/leagues?id=73",
            "https://www.fotmob.com/api/leagues?id=113",
            "https://www.fotmob.com/api/leagues?id=273",
            "https://www.fotmob.com/api/leagues?id=120",
            "https://www.fotmob.com/api/leagues?id=274",
            "https://www.fotmob.com/api/leagues?id=252",
            "https://www.fotmob.com/api/leagues?id=122",
            "https://www.fotmob.com/api/leagues?id=108",
            "https://www.fotmob.com/api/leagues?id=109",
            "https://www.fotmob.com/api/leagues?id=230",
            "https://www.fotmob.com/api/leagues?id=189",
            "https://www.fotmob.com/api/leagues?id=182",
            "https://www.fotmob.com/api/leagues?id=64",
            "https://www.fotmob.com/api/leagues?id=223"
            ]

start_game_url = "https://www.fotmob.com/api/matchDetails?matchId="

today_games = []

todays_date = "2023-09-04"

df = pd.DataFrame({'Date': pd.Series(dtype='str'),
                   'League': pd.Series(dtype='str'),
                   'Country': pd.Series(dtype='str'),
                   'HomeTeam': pd.Series(dtype='str'),
                   'AwayTeam': pd.Series(dtype='str'),
                   'fairHomeOdds': pd.Series(dtype='float'),
                   'fairDrawOdds': pd.Series(dtype='float'),
                   'fairAwayOdds': pd.Series(dtype='float'),
                   'fairOverOdds': pd.Series(dtype='float'),
                   'fairUnderOdds': pd.Series(dtype='float'),
                   'fairBTTSOdds': pd.Series(dtype='float'),
                   'fairnBTTSOdds': pd.Series(dtype='float')
                   })

i = 1

for link in url_list:
    res = requests.get(link)
    jasondata = res.json()

    for match in jasondata['matches']['allMatches']:
        try:
            game_id = match['id']
            finished = match['status']['finished']
            cancelled = match['status']['cancelled']
            date = match['status']['utcTime'].split("T")[0]

            query = f"SELECT * FROM Games WHERE match_id = {game_id}"
            in_database = call_db(query)

            if not finished and not cancelled and not in_database and date == todays_date:
                today_games.append(game_id)

            

        except KeyError:
            pass

    print("Getting League:",i,"/",len(url_list))
    i = i + 1

        

i = 1

matchups = []

for game_id in today_games:

    game_url = start_game_url + str(game_id)
    fot_res = requests.get(game_url)
    jasondata = fot_res.json()

    HomeTeam = jasondata['general']['homeTeam']['name'].replace("'"," ")
    AwayTeam = jasondata['general']['awayTeam']['name'].replace("'"," ")
    League = jasondata['general']['parentLeagueName']
    Time = jasondata['general']['matchTimeUTCDate'].split("T")[1][:5]
    Country = jasondata['general']['countryCode']
    hour = int(Time[:2])
    hour += 1
    hour_string = str(hour).zfill(2)
    Time = hour_string + Time[2:]

    matchups.append(Time+"_"+HomeTeam+"_"+AwayTeam+"_"+League+"_"+Country)

    print("Getting Game:",i,"/",len(today_games))
    i = i + 1



matchups.sort()



i = 1

for matchup in matchups:
    try:
        Time = matchup.split("_")[0]
        HomeTeam = matchup.split("_")[1]
        AwayTeam = matchup.split("_")[2]
        League = matchup.split("_")[3]
        Country = matchup.split("_")[4]
        
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

        get_home_games = f"SELECT COUNT(id) FROM Games WHERE HomeTeam = '{HomeTeam}' AND Country = '{Country}'"
        home_count = get_value(get_home_games)

        get_away_games = f"SELECT COUNT(id) FROM Games WHERE AwayTeam = '{AwayTeam}' AND Country = '{Country}'"
        away_count = get_value(get_away_games)
        

        print("----------")
        print(League,"|",Country,"(",count,")","(",home_count,")","(",away_count,")")
        print(Time,"|", todays_date)
        
        print(HomeTeam, home_odds,"(",round(home_win_pct,2),"% )")
        print("Draw", draw_odds,"(",round(draw_pct,2),"% )")
        print(AwayTeam, away_odds,"(",round(away_win_pct,2),"% )")
        

        
        print("Over 2.5 goals:",over_2_5_odds,"(",round(over_2_5_pct,2),"% )")
        print("Under 2.5 goals:",under_2_5_odds,"(",round(under_2_5_pct,2),"% )")
        

        
        print("BTTS:",btts_odds,"(",round(btts_pct,2),"% )")
        print("NOT BTTS:",no_btts_odds,"(",round(no_btts_pct,2),"% )")
        

        
        print("Most common result:", most_common_result, most_common_result_odds,"(",round(most_common_result_pct,2),"% )" )
     

        string = "_".join([str(todays_date), str(Time), str(League), str(HomeTeam), str(AwayTeam)]).replace(":","")

        

        HomeCorner = round(xStats['HomeCor'],2)
        AwayCorner = round(xStats['AwayCor'],2)
        TotalCorners = round(HomeCorner + AwayCorner, 2)
        CornerHCP = round(xStats['AwayCor'] - xStats['HomeCor'],2)


        new_row = {
                'Date': [todays_date],
                'League': [League],
                'Country': [Country],
                'HomeTeam': [HomeTeam],
                'AwayTeam': [AwayTeam],
                'fairHomeOdds': [home_odds],
                'fairDrawOdds': [draw_odds],
                'fairAwayOdds': [away_odds],
                'fairOverOdds': [over_2_5_odds],
                'fairUnderOdds': [under_2_5_odds],
                'fairBTTSOdds': [btts_odds],
                'fairnBTTSOdds': [no_btts_odds]
        }
       
        # df = df.append(new_row)
        df.loc[len(df.index)] = [todays_date, League, Country, HomeTeam, AwayTeam, home_odds, draw_odds, away_odds, over_2_5_odds, under_2_5_odds, btts_odds, no_btts_odds]
        


        try:
            file = open("Game_Stats/" + string + ".txt", "w")
            file.write(League + " | " + Country + " ( " + str(count) + " )" + " ( " + str(home_count) + " )" + " ( " + str(away_count) + " )\n")
            file.write(Time + " | " + todays_date + "\n")
            file.write("---------------------------------------" + "\n")
            file.write(HomeTeam + " " + str(home_odds) + " ( " + str(round(home_win_pct, 2)) + " % ) \n")
            file.write("Draw " + str(draw_odds) + " ( " + str(round(draw_pct, 2)) + " % ) \n")
            file.write(AwayTeam + " " + str(away_odds) + " ( " + str(round(away_win_pct, 2)) + " % ) \n")
            file.write("---------------------------------------" + "\n")
            file.write("Over 2.5 goals: " + str(over_2_5_odds) + " ( " + str(round(over_2_5_pct, 2)) + " % ) \n")
            file.write("Under 2.5 goals: " + str(under_2_5_odds) + " ( " + str(round(under_2_5_pct, 2)) + " % ) \n")
            file.write("---------------------------------------" + "\n")
            file.write("BTTS: " + str(btts_odds) + " ( " + str(round(btts_pct, 2)) + " % ) \n")
            file.write("NOT BTTS: " + str(no_btts_odds) + " ( " + str(round(no_btts_pct, 2)) + " % ) \n")
            file.write("---------------------------------------" + "\n")
            file.write("Most common result: " + str(most_common_result) + " " + str(most_common_result_odds) + " ( " + str(round(most_common_result_pct, 2)) + " % ) \n")
            file.write("---------------------------------------" + "\n")
            file.write("Home Corners: " + str(HomeCorner) + "\n")
            file.write("Away Corners: " + str(AwayCorner) + "\n")
            file.write("Total Corners: " + str(TotalCorners) + "\n")
            file.write("Corner HCP: " + str(CornerHCP) + "\n")

            file.close()
        except:
            pass

        
        # print("Home Corners:", hxCor)
        # print("Away Corners:", axCor)
        # print("Total Corners:", round(hxCor+axCor,2))
        # print("Corner HCP:", round(axCor - hxCor,2))
    except:
        pass

df.to_csv("odds.csv", index=False)