import requests
import json

match_url = "https://www.fotmob.com/api/matchDetails?matchId=4084714"

res = requests.get(match_url)
jasondata = res.json()

game_id = jasondata['general']['matchId']



for i in range(0,2):
    for j in range(0,11):
        for k in range(0,11):

            try:    
                player_dict = {"Name": [],
               "Position": [],
               "Status": [],
               "Top Stats": [],
               "Attack Stats": [],
               "Defence Stats": [],
               "Duel Stats": []
               }
                
                name = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['name']['fullName']
                
                position = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['positionStringShort']

                player_dict["Name"].append(name)
                player_dict["Position"].append(position)
                player_dict["Status"].append("Starter")
            

                try:
                    top_stats = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['stats'][0]['stats']
                    player_dict["Top Stats"].append(top_stats)
                except:
                    # top_stats = "NULL"
                    player_dict["Top Stats"].append("NULL")
            
                try:
                    attack_stats = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['stats'][1]['stats']
                    player_dict["Attack Stats"].append(attack_stats)
                except:
                    # attack_stats = "NULL"
                    player_dict["Attack Stats"].append("NULL")
            
                try:    
                    defence_stats = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['stats'][2]['stats']
                    player_dict["Defence Stats"].append(defence_stats)
                except:
                    # defence_stats = "NULL"
                    player_dict["Defence Stats"].append("NULL")
            
                try:
                    duel_stats= jasondata['content']['lineup']['lineup'][i]['players'][j][k]['stats'][3]['stats']
                    player_dict["Duel Stats"].append(duel_stats)
                except:
                    # duel_stats = "NULL"
                    player_dict["Duel Stats"].append("NULL")

                print(player_dict)
                print("-------------------------------------")

                if player_dict['Position'] == 'GK':
                    pass

                else:
                    pass

            except:
                pass


                
        
        




