import requests
import json
from db import *

def get_starter_stats(id):

    

    match_url = "https://www.fotmob.com/api/matchDetails?matchId=" + str(id)

    res = requests.get(match_url)
    jasondata = res.json()

    game_id = jasondata['general']['matchId']
    game_date = jasondata['general']['matchTimeUTCDate'].split('T')[0]

    goals_min_home = []
    goals_min_away = []


    for i in range(0,100):

        try:
            event = jasondata['content']['matchFacts']['events']['events'][i]['type']
            is_home = jasondata['content']['matchFacts']['events']['events'][i]['isHome']

            if event == 'Goal' and is_home == True:
                time = jasondata['content']['matchFacts']['events']['events'][i]['time']
                goals_min_home.append(time)

            if event == 'Goal' and is_home == False:
                time = jasondata['content']['matchFacts']['events']['events'][i]['time']
                goals_min_away.append(time)    
        except:
            pass


    for i in range(0,2):
        for j in range(0,12):
            for k in range(0,12):

                try:    
                #     player_dict = {"Name": [],
                #    "Position": [],
                #    "Status": [],
                #    "Top Stats": []
                #    }
                    
                    match_id = game_id

                    player_id = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['id']

                    if i == 0:
                        home_away = 'Home'
                    if i != 0:
                        home_away = 'Away'

                    status = 'Starter'

                    name = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['name']['fullName']
                    
                    position = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['positionStringShort']

                    role = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['role']

                    start_min = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['timeSubbedOn']

                    end_min = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['timeSubbedOff']

                    if start_min is None:
                        start_min = 0

                    if end_min is None:
                        end_min = 90

                    total_min = end_min - start_min

                    if home_away == 'Home':
                        goals_for = 0
                        goals_against = 0
                        for goal in goals_min_home:
                            if start_min < goal < end_min:
                                goals_for += 1
                        for goal in goals_min_away:
                            if start_min < goal < end_min:
                                goals_against += 1

                    if home_away == 'Away':
                        goals_for = 0
                        goals_against = 0
                        for goal in goals_min_away:
                            if start_min < goal < end_min:
                                goals_for += 1
                        for goal in goals_min_home:
                            if start_min < goal < end_min:
                                goals_against += 1
                

                    try:
                        goals = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['stats'][0]['stats']['Goals']
                    except:
                        goals = 0

                    try:
                        assists = jasondata['content']['lineup']['lineup'][i]['players'][j][k]['stats'][0]['stats']['Assists']
                    except:
                        assists = 0

                    query = f"""
                    INSERT INTO Players (match_id, date, player_id, HA, status, name, position, role, total_min, goals, assists, goals_for, goals_against)
                    VALUES ({match_id}, '{game_date}', {player_id}, '{home_away}', '{status}', '{name}', '{position}', '{role}', {total_min}, {goals}, {assists}, {goals_for}, {goals_against})
                    """

                    call_db(query)

                except:
                    pass

def get_bench_stats(id):

    

    match_url = "https://www.fotmob.com/api/matchDetails?matchId=" + str(id)

    res = requests.get(match_url)
    jasondata = res.json()

    game_id = jasondata['general']['matchId']
    game_date = jasondata['general']['matchTimeUTCDate'].split('T')[0]

    goals_min_home = []
    goals_min_away = []



    for i in range(0,100):


        try:
            event = jasondata['content']['matchFacts']['events']['events'][i]['type']
            is_home = jasondata['content']['matchFacts']['events']['events'][i]['isHome']

            if event == 'Goal' and is_home == True:
                time = jasondata['content']['matchFacts']['events']['events'][i]['time']
                goals_min_home.append(time)

            if event == 'Goal' and is_home == False:
                time = jasondata['content']['matchFacts']['events']['events'][i]['time']
                goals_min_away.append(time)    
        except:
            pass


    for i in range(0,2):
        for j in range(0,12):

            try:
                
                match_id = game_id

                player_id = jasondata['content']['lineup']['bench']['benchArr'][i][j]['id']

                if i == 0:
                    home_away = 'Home'
                if i != 0:
                    home_away = 'Away'

                status = 'Bench'

                name = jasondata['content']['lineup']['bench']['benchArr'][i][j]['name']['fullName']

                position = "NULL"
                
                role = jasondata['content']['lineup']['bench']['benchArr'][i][j]['role']

                start_min = jasondata['content']['lineup']['bench']['benchArr'][i][j]['timeSubbedOn']

                end_min = jasondata['content']['lineup']['bench']['benchArr'][i][j]['timeSubbedOff']

                

                if start_min is None:
                    start_min = 90

                if end_min is None:
                    end_min = 90

                total_min = end_min - start_min

                if home_away == 'Home':
                    goals_for = 0
                    goals_against = 0
                    for goal in goals_min_home:
                        if start_min < goal < end_min:
                            goals_for += 1
                    for goal in goals_min_away:
                        if start_min < goal < end_min:
                            goals_against += 1

                if home_away == 'Away':
                    goals_for = 0
                    goals_against = 0
                    for goal in goals_min_away:
                        if start_min < goal < end_min:
                            goals_for += 1
                    for goal in goals_min_home:
                        if start_min < goal < end_min:
                            goals_against += 1
            

                try:
                    goals = jasondata['content']['lineup']['bench']['benchArr'][i][j]['stats'][0]['stats']['Goals']
                except:
                    goals = 0

                try:
                    assists = jasondata['content']['lineup']['bench']['benchArr'][i][j]['stats'][0]['stats']['Assists']
                except:
                    assists = 0


                query = f"""
                    INSERT INTO Players (match_id, date, player_id, HA, status, name, position, role, total_min, goals, assists, goals_for, goals_against)
                    VALUES ({match_id}, '{game_date}', {player_id}, '{home_away}', '{status}', '{name}', '{position}', '{role}', {total_min}, {goals}, {assists}, {goals_for}, {goals_against})
                """

                call_db(query)

            except:
                pass

get_bench_stats(4084714)