import json
from db import call_db, get_value
import os
import shutil


folder_path = "C:/Users/simon/Documents/GitHub/Python_2023/Mina_egna/scrape1602/Stats/"

for filename in os.listdir(folder_path):
    if filename.endswith(".json"): # Replace with the file extension you want to run the program for
        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            with open(file_path, encoding='utf-8') as f:
                # Do something with the file
                jasondata = json.load(f)



                match_id = jasondata['general']['matchId']
                print(match_id)
                # bench_players = []

                

                # for i in range(len(jasondata['content']['lineup']['lineup'][0]['bench'])):

                #     try:
                #         player_first_name = jasondata['content']['lineup']['lineup'][0]['bench'][i]['name']['firstName']
                #         player_last_name = jasondata['content']['lineup']['lineup'][0]['bench'][i]['name']['lastName']
                #         minutes_played = jasondata['content']['lineup']['lineup'][0]['bench'][i]['minutesPlayed']
                #         goals = jasondata['content']['lineup']['lineup'][0]['bench'][i]['stats'][0]['stats']['Goals']
                #         assists = jasondata['content']['lineup']['lineup'][0]['bench'][i]['stats'][0]['stats']['Assists']
                #         player_name = player_first_name + " " + player_last_name

                #         player_dict = {}
                #         player_dict["Name"] = player_name
                #         player_dict["Minutes"] = minutes_played
                #         player_dict["Goals"] = goals
                #         player_dict["Assists"] = assists

                #         bench_players.append(player_dict)
                #     except:
                #         pass
               

                # start_players = []
                
                
                # for i in range(0,100):
                #     for j in range(0,100):
                #         try:

                #             try:
                #                 first_name = jasondata['content']['lineup']['lineup'][j]['players'][i][0]['name']['firstName']
                #             except:
                #                 first_name = ""

                #             try:
                #                 last_name = jasondata['content']['lineup']['lineup'][j]['players'][i][0]['name']['lastName']
                #             except:
                #                 last_name = ""

                #             try:
                #                 minutes_played = jasondata['content']['lineup']['lineup'][j]['players'][i][0]['minutesPlayed']
                #             except:
                #                 minutes_played = 0
                #             try:
                #                 goals = jasondata['content']['lineup']['lineup'][j]['players'][i][0]['stats'][0]['stats']['Goals']
                #             except:
                #                 goals = 0
                #             try:
                #                 assists = jasondata['content']['lineup']['lineup'][j]['players'][i][0]['stats'][0]['stats']['Assists']
                #             except:
                #                 assists = 0
                #             player_name = first_name + " " + last_name
                            

                #             player_dict = {}
                #             player_dict["Name"] = player_name
                #             player_dict["Minutes"] = minutes_played
                #             player_dict["Goals"] = goals
                #             player_dict["Assists"] = assists
                            

                #             start_players.append(player_dict)

                #         except:
                #             pass
                           
                # filtered_data = [d for d in start_players if d['Name'].strip() == ' ']

                # print(filtered_data)
                # print(len(filtered_data))
