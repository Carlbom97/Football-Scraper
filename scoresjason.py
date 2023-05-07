import json
from db import call_db, get_value
import os
import shutil


folder_path = "C:/Users/simon/Documents/GitHub/Python_2023/Mina_egna/scrape1602/Stats" # Replace with the path to your folder
# folder_path2 = "C:/Users/simon/Documents/GitHub/Python_2023/Mina_egna/scrape1602/id_date"

# for filename in os.listdir(folder_path2):
#                     if filename.endswith(".json"): # Replace with the file extension you want to run the program for
#                         file_path2 = os.path.join(folder_path2, filename)
#                         if os.path.exists(file_path2):
#                             with open(file_path2) as f:
#                                 # Do something with the file
#                                 jasondata = json.load(f)
#                                 file = filename

#                                 date = file.split(".")[0]
#                                 League = jasondata['events'][0]['tournament']['name']
#                                 Country = jasondata['events'][0]['tournament']['category']['name']
#                                 HomeTeam = jasondata['events'][0]['homeTeam']['name']
#                                 AwayTeam = jasondata['events'][0]['awayTeam']['name']
#                                 HGoals = jasondata['events'][0]['homeScore']['current']
#                                 AGoals = jasondata['events'][0]['awayScore']['current']
                            
#                             os.remove(file_path2)


for filename in os.listdir(folder_path):
    if filename.endswith(".json"): # Replace with the file extension you want to run the program for
        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            with open(file_path) as f:
                # Do something with the file
                jasondata = json.load(f)
                file = filename
                
                league_id = file.split("_")[1]
                home_team_id = file.split("_")[2]
                away_team_id = file.split("_")[3]


                date = file.split("_")[0]
                League = get_value(f"SELECT League FROM Leagues WHERE id = {league_id}")
                Country = get_value(f"SELECT Nation FROM Leagues WHERE id = {league_id}")
                HomeTeam = get_value(f"SELECT Team From Teams WHERE id = {home_team_id}")
                AwayTeam = get_value(f"SELECT Team From Teams WHERE id = {away_team_id}")
                HGoals = file.split("_")[4]
                AGoals = file.split("_")[5].split(".")[0]

                stats = {}

                #POSSESION
                try: 
                    stat_name = jasondata['statistics'][0]['groups'][0]['statisticsItems'][0]['name']
                    home_stat = jasondata['statistics'][0]['groups'][0]['statisticsItems'][0]['home']
                    away_stat = jasondata['statistics'][0]['groups'][0]['statisticsItems'][0]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try: 
                    stat_name = jasondata['statistics'][0]['groups'][0]['statisticsItems'][1]['name']
                    home_stat = jasondata['statistics'][0]['groups'][0]['statisticsItems'][1]['home']
                    away_stat = jasondata['statistics'][0]['groups'][0]['statisticsItems'][1]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try: 
                    stat_name = jasondata['statistics'][0]['groups'][0]['statisticsItems'][2]['name']
                    home_stat = jasondata['statistics'][0]['groups'][0]['statisticsItems'][2]['home']
                    away_stat = jasondata['statistics'][0]['groups'][0]['statisticsItems'][2]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                #SHOTS
                try:
                    stat_name = jasondata['statistics'][0]['groups'][1]['statisticsItems'][0]['name']
                    home_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][0]['home']
                    away_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][0]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][1]['statisticsItems'][1]['name']
                    home_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][1]['home']
                    away_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][1]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][1]['statisticsItems'][2]['name']
                    home_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][2]['home']
                    away_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][2]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][1]['statisticsItems'][3]['name']
                    home_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][3]['home']
                    away_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][3]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][1]['statisticsItems'][4]['name']
                    home_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][4]['home']
                    away_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][4]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][1]['statisticsItems'][5]['name']
                    home_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][5]['home']
                    away_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][5]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][1]['statisticsItems'][6]['name']
                    home_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][6]['home']
                    away_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][6]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][1]['statisticsItems'][7]['name']
                    home_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][7]['home']
                    away_stat = jasondata['statistics'][0]['groups'][1]['statisticsItems'][7]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                #CORNERS ETC
                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][0]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][0]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][0]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][1]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][1]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][1]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][2]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][2]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][2]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][3]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][3]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][3]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][4]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][4]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][4]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][5]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][5]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][5]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][6]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][6]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][6]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][7]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][7]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][7]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][8]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][8]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][8]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][2]['statisticsItems'][9]['name']
                    home_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][9]['home']
                    away_stat = jasondata['statistics'][0]['groups'][2]['statisticsItems'][9]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                #CORNERS ETC
                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][0]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][0]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][0]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][1]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][1]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][1]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][2]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][2]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][2]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][3]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][3]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][3]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][4]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][4]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][4]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][5]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][5]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][5]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][6]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][6]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][6]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][7]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][7]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][7]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][8]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][8]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][8]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][3]['statisticsItems'][9]['name']
                    home_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][9]['home']
                    away_stat = jasondata['statistics'][0]['groups'][3]['statisticsItems'][9]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                #PASSES ETC
                try:
                    stat_name = jasondata['statistics'][0]['groups'][4]['statisticsItems'][0]['name']
                    home_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][0]['home']
                    away_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][0]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][4]['statisticsItems'][1]['name']
                    home_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][1]['home']
                    away_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][1]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][4]['statisticsItems'][2]['name']
                    home_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][2]['home']
                    away_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][2]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][4]['statisticsItems'][3]['name']
                    home_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][3]['home']
                    away_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][3]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][4]['statisticsItems'][4]['name']
                    home_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][4]['home']
                    away_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][4]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][4]['statisticsItems'][5]['name']
                    home_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][5]['home']
                    away_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][5]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][4]['statisticsItems'][6]['name']
                    home_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][6]['home']
                    away_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][6]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][4]['statisticsItems'][7]['name']
                    home_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][7]['home']
                    away_stat = jasondata['statistics'][0]['groups'][4]['statisticsItems'][7]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                #DRIBBLE ETC
                try:
                    stat_name = jasondata['statistics'][0]['groups'][5]['statisticsItems'][0]['name']
                    home_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][0]['home']
                    away_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][0]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][5]['statisticsItems'][1]['name']
                    home_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][1]['home']
                    away_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][1]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][5]['statisticsItems'][2]['name']
                    home_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][2]['home']
                    away_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][2]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][5]['statisticsItems'][3]['name']
                    home_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][3]['home']
                    away_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][3]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][5]['statisticsItems'][4]['name']
                    home_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][4]['home']
                    away_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][4]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][5]['statisticsItems'][5]['name']
                    home_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][5]['home']
                    away_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][5]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][5]['statisticsItems'][6]['name']
                    home_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][6]['home']
                    away_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][6]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][5]['statisticsItems'][7]['name']
                    home_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][7]['home']
                    away_stat = jasondata['statistics'][0]['groups'][5]['statisticsItems'][7]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass
                #TACKLE ETC
                try:
                    stat_name = jasondata['statistics'][0]['groups'][6]['statisticsItems'][0]['name']
                    home_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][0]['home']
                    away_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][0]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][6]['statisticsItems'][1]['name']
                    home_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][1]['home']
                    away_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][1]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][6]['statisticsItems'][2]['name']
                    home_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][2]['home']
                    away_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][2]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                #TACKLE ETC
                try:
                    stat_name = jasondata['statistics'][0]['groups'][6]['statisticsItems'][3]['name']
                    home_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][3]['home']
                    away_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][3]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][6]['statisticsItems'][4]['name']
                    home_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][4]['home']
                    away_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][4]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][6]['statisticsItems'][5]['name']
                    home_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][5]['home']
                    away_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][5]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                #TACKLE ETC
                try:
                    stat_name = jasondata['statistics'][0]['groups'][6]['statisticsItems'][6]['name']
                    home_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][6]['home']
                    away_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][6]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][6]['statisticsItems'][7]['name']
                    home_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][7]['home']
                    away_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][7]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][6]['statisticsItems'][8]['name']
                    home_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][8]['home']
                    away_stat = jasondata['statistics'][0]['groups'][6]['statisticsItems'][8]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][7]['statisticsItems'][0]['name']
                    home_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][0]['home']
                    away_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][0]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][7]['statisticsItems'][1]['name']
                    home_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][1]['home']
                    away_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][1]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][7]['statisticsItems'][2]['name']
                    home_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][2]['home']
                    away_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][2]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                #TACKLE ETC
                try:
                    stat_name = jasondata['statistics'][0]['groups'][7]['statisticsItems'][3]['name']
                    home_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][3]['home']
                    away_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][3]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][7]['statisticsItems'][4]['name']
                    home_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][4]['home']
                    away_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][4]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][7]['statisticsItems'][5]['name']
                    home_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][5]['home']
                    away_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][5]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                #TACKLE ETC
                try:
                    stat_name = jasondata['statistics'][0]['groups'][7]['statisticsItems'][6]['name']
                    home_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][6]['home']
                    away_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][6]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][7]['statisticsItems'][7]['name']
                    home_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][7]['home']
                    away_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][7]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass

                try:
                    stat_name = jasondata['statistics'][0]['groups'][7]['statisticsItems'][8]['name']
                    home_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][8]['home']
                    away_stat = jasondata['statistics'][0]['groups'][7]['statisticsItems'][8]['away']

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass


                print(stats)

                try:
                    HomexG = stats['HomeExpectedgoals'].replace("%","")
                except:
                    HomexG = 0

                try:
                    AwayxG = stats['AwayExpectedgoals'].replace("%","")
                except:
                    AwayxG = 0

                try:
                    HomePoss = stats['HomeBallpossession'].replace("%","")
                except:
                    HomePoss = 0

                try:
                    AwayPoss = stats['AwayBallpossession'].replace("%","")
                except:
                    AwayPoss = 0

                try:
                    HomeShots = stats['HomeTotalshots']
                except:
                    HomeShots = 0

                try:
                    AwayShots = stats['AwayTotalshots']
                except:
                    AwayShots = 0

                try:
                    HomeSont = stats['HomeShotsontarget']
                except:
                    HomeSont = 0

                try:
                    AwaySonT = stats['AwayShotsontarget']
                except:
                    AwaySonT = 0

                try:
                    HomeSoffT = stats['HomeShotsofftarget']
                except:
                    HomeSoffT = 0

                try:
                    AwaySoffT = stats['AwayShotsofftarget']
                except:
                    AwaySoffT = 0

                try:
                    HomeBS = stats['HomeBlockedshots']
                except:
                    HomeBS = 0

                try:
                    AwayBS = stats['AwayBlockedshots']
                except:
                    AwayBS = 0

                try:
                    HomeCor = stats['HomeCornerkicks']
                except:
                    HomeCor = 0

                try:
                    AwayCor = stats['AwayCornerkicks']
                except:
                    AwayCor = 0

                try:
                    HomeOff = stats['HomeOffsides']
                except:
                    HomeOff = 0

                try:
                    AwayOff = stats['AwayOffsides']
                except:
                    AwayOff = 0

                try:
                    HomeFoul = stats['HomeFouls']
                except:
                    HomeFoul = 0

                try:
                    AwayFoul = stats['AwayFouls']
                except:
                    AwayFoul = 0

                try:
                    HomeYellow = stats['HomeYellowcards']
                except:
                    HomeYellow = 0

                try:
                    AwayYellow = stats['AwayYellowcards']
                except:
                    AwayYellow = 0

                try:
                    HomeRed = stats['HomeRedcards']
                except:
                    HomeRed = 0

                try:
                    AwayRed = stats['AwayRedcards']
                except:
                    AwayRed = 0

                try:
                    HomePass = stats['HomePasses']
                except:
                    HomePass = 0

                try:
                    AwayPass = stats['AwayPasses']
                except:
                    AwayPass = 0

                try:
                    HomeAccPass = stats['HomeAccuratepasses'].split(" ")[0]
                except:
                    HomeAccPass = 0

                try:
                    AwayAccPass = stats['AwayAccuratepasses'].split(" ")[0]
                except:
                    AwayAccPass = 0

                try:
                    HomeLongB = stats['HomeLongballs'].split("/")[0]
                except:
                    HomeLongB = 0

                try:
                    AwayLongB = stats['AwayLongballs'].split("/")[0]
                except:
                    AwayLongB = 0

                try:
                    HomeAccLongB = stats['HomeLongballs'].split("/")[1].split(" ")[0]
                except:
                    HomeAccLongB = 0

                try:
                    AwayAccLongB = stats['AwayLongballs'].split("/")[1].split(" ")[0]
                except:
                    AwayAccLongB = 0

                try:
                    HomeCross = stats['HomeCrosses'].split("/")[0]
                except:
                    HomeCross = 0

                try:
                    AwayCross = stats['AwayCrosses'].split("/")[0]
                except:
                    AwayCross = 0

                try:
                    HomeAccCross = stats['HomeCrosses'].split("/")[1].split(" ")[0]
                except:
                    HomeAccCross = 0

                try:
                    AwayAccCross = stats['AwayCrosses'].split("/")[1].split(" ")[0]
                except:
                    AwayAccCross = 0

                try:
                    HomeDribb = stats['HomeDribbles'].split("/")[0]
                except:
                    HomeDribb = 0

                try:
                    AwayDribb = stats['AwayDribbles'].split("/")[0]
                except:
                    AwayDribb = 0

                try:
                    HomeAccDribb = stats['HomeDribbles'].split("/")[1].split(" ")[0]
                except:
                    HomeAccDribb = 0

                try:
                    AwayAccDribb = stats['AwayDribbles'].split("/")[1].split(" ")[0]
                except:
                    AwayAccDribb = 0

                try:
                    HomePossLost = stats['HomePossessionlost']
                except:
                    HomePossLost = 0

                try:
                    AwayPossLost = stats['AwayPossessionlost']
                except:
                    AwayPossLost = 0

                try:
                    HomeDuelsW = stats['HomeDuelswon']
                except:
                    HomeDuelsW = 0

                try:
                    AwayDuelsW = stats['AwayDuelswon']
                except:
                    AwayDuelsW = 0

                try:
                    HomeAerialsW = stats['HomeAerialswon']
                except:
                    HomeAerialsW = 0

                try:
                    AwayAerialsW = stats['AwayAerialswon']
                except:
                    AwayAerialsW = 0

                try:
                    HomeTack = stats['HomeTackles']
                except:
                    HomeTack = 0

                try:
                    AwayTack = stats['AwayTackles']
                except:
                    AwayTack = 0

                try:
                    HomeInt = stats['HomeInterceptions']
                except:
                    HomeInt = 0

                try:
                    AwayInt = stats['AwayInterceptions']
                except:
                    AwayInt = 0

                try:
                    HomeClear = stats['HomeClearances']
                except:
                    HomeClear = 0

                try:
                    AwayClear = stats['AwayClearances']
                except:
                    AwayClear = 0

                query = f"""
                    INSERT INTO Games (date, Country, League, HomeTeam, AwayTeam, HGoals, AGoals, HomexG, AwayxG, HomePoss, AwayPoss, HomeShots, AwayShots, HomeSonT, AwaySonT, HomeSoffT, AwaySoffT, HomeBS, AwayBS, HomeCor, AwayCor, HomeOff, AwayOff, HomeFoul, AwayFoul, HomeYellow, AwayYellow, HomeRed, AwayRed, HomePass, AwayPass, HomeAccPass, AwayAccPass, HomeLongB, AwayLongB, HomeAccLongB, AwayAccLongB, HomeCross, AwayCross, HomeAccCross, AwayAccCross, HomeDribb, AwayDribb, HomeAccDribb, AwayAccDribb, HomePossLost, AwayPossLost, HomeDuelsW, AwayDuelsW, HomeAerialsW, AwayAerialsW, HomeTack, AwayTack, HomeInt, AwayInt, HomeClear, AwayClear)
                    VALUES ('{date}', '{Country}', '{League}', '{HomeTeam}', '{AwayTeam}', {HGoals}, {AGoals}, {HomexG}, {AwayxG}, {HomePoss}, {AwayPoss}, {HomeShots}, {AwayShots}, {HomeSont}, {AwaySonT}, {HomeSoffT}, {AwaySoffT}, {HomeBS}, {AwayBS}, {HomeCor}, {AwayCor}, {HomeOff}, {AwayOff}, {HomeFoul}, {AwayFoul}, {HomeYellow}, {AwayYellow}, {HomeRed}, {AwayRed}, {HomePass}, {AwayPass}, {HomeAccPass}, {AwayAccPass}, {HomeLongB}, {AwayLongB}, {HomeAccLongB}, {AwayAccLongB}, {HomeCross}, {AwayCross}, {HomeAccCross}, {AwayAccCross}, {HomeDribb}, {AwayDribb}, {HomeAccDribb}, {AwayAccDribb}, {HomePossLost}, {AwayPossLost}, {HomeDuelsW}, {AwayDuelsW}, {HomeAerialsW}, {AwayAerialsW}, {HomeTack}, {AwayTack}, {HomeInt}, {AwayInt}, {HomeClear}, {AwayClear})
                """

                call_db(query)

                path = f"C:/Users/simon/Documents/GitHub/Python_2023/Mina_egna/scrape1602/Leagues/{League}"

                if not os.path.exists(path):
                    os.makedirs(path)
                    print(f"{League} directory created successfully!")

                date_path = os.path.join(path, date)

                if not os.path.exists(date_path):
                    os.makedirs(date_path)
                    print(f"{date} directory created successfully!")
                else:
                    print(f"{date} directory already exists!")

                # det_folder = f"C:/Users/simon/Documents/GitHub/Python_2023/Mina_egna/scrape1602/Leagues/{League}/{date}"


                f.close()

                file_name = file
                new_name = date +"_"+ HomeTeam +"_"+ AwayTeam +"_"+ str(HGoals) +"_"+ str(AGoals) +"_"+ League.replace(" ","") +"_"+ Country.replace(" ","")+".json"

                dir_path = os.path.dirname(file_path)
                new_file_path = os.path.join(dir_path, new_name)

                os.rename(file_path, new_file_path)
                

                det_folder = date_path

                source_file_path = os.path.join(folder_path, new_name)
                destination_file_path = os.path.join(det_folder, new_name)
                shutil.move(source_file_path, destination_file_path)

        else:
            print(f"File {file_path} does not exist")