import requests
from db import call_db, get_value
from regression import stats_list, home_stats_list, away_stats_list, get_coefficients

url = "https://www.fotmob.com/api/leagues?id=67"

data = requests.get(url)

jasondata = data.json()

game_ids = []

for match in jasondata['matches']['allMatches']:
        try:
            game_id = match['id']
            game_ids.append(game_id)
        except KeyError:
            pass

print(len(game_ids))

start_game_url = "https://www.fotmob.com/api/matchDetails?matchId="

games = []

i = 1

for game in game_ids:
    game_url = start_game_url+str(game)

    data = requests.get(game_url)
    jasondata = data.json()

    HomeTeam = jasondata['general']['homeTeam']['name'].replace("'"," ")
    AwayTeam = jasondata['general']['awayTeam']['name'].replace("'"," ")

    date = jasondata['general']['matchTimeUTCDate'].split("T")[0]

    string = "_".join([str(date), str(HomeTeam), str(AwayTeam)])

    games.append(string)

    print(i,"/",len(game_ids))

    i += 1

games.sort()

result = get_coefficients()

games_xg = []

i = 1

for game in games:
    try:

        HomeTeam = game.split("_")[1]
        AwayTeam = game.split("_")[2]
        League = "Allsvenskan"
        
        home_coeff = result[0]
        away_coeff = result[1]
        
        league_stats = {}
        home_stats = {}
        away_stats = {}

        
        
        for stat in stats_list:
        # Goals scored

        
            home_avr = f"SELECT AVG({stat}) FROM Games WHERE HomeTeam = '{HomeTeam}' AND League = '{League}' AND {stat} IS NOT NULL"
            home_avr = get_value(home_avr)
            home_avr = round(home_avr, 2)
                
            home_stats[stat] = home_avr

        
            home_avr = f"SELECT AVG({stat}) FROM Games WHERE HomeTeam = '{HomeTeam}' AND {stat} IS NOT NULL"
            home_avr = get_value(home_avr)
            home_avr = round(home_avr, 2)
                
            home_stats[stat] = home_avr

            

        for stat in stats_list:
        #Goals scoerd
            
            away_avr = f"SELECT AVG({stat}) FROM Games WHERE AwayTeam = '{AwayTeam}' AND League = '{League}' AND {stat} IS NOT NULL"
            away_avr = get_value(away_avr)
            
            away_avr = round(away_avr, 2)

            away_stats[stat] = away_avr
            

            

        for stat in stats_list:
        #Goals scoerd
            league_avr = f"SELECT AVG({stat}) FROM Games WHERE League = '{League}' AND {stat} IS NOT NULL"
            league_avr = get_value(league_avr)
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
            
            xg = home_coeff[stat] * xStats[stat]
            Home_xG = Home_xG + xg
            

        for stat in stats_list:
            
            xg = away_coeff[stat] * xStats[stat]
            Away_xG = Away_xG + xg

        Home_xG = round(Home_xG,2)
        Away_xG = round(Away_xG,2)

        string = "_".join([str(date), str(HomeTeam), str(AwayTeam),str(Home_xG), str(Away_xG)])


        games_xg.append(string)

        print("Calculated xG:",i,"/",len(games))
        i += 1
    except:
        print("Calculated xG:",i,"/",len(games),"ERROR!")
        i += 1

    

for row in games_xg:
    print(row) 