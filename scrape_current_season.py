import requests
from db import call_db
import json
import os
from player2 import *


url_list = ["https://www.fotmob.com/api/leagues?id=47", # Premier League
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
            "https://www.fotmob.com/api/leagues?id=10216", # Conference League
            "https://www.fotmob.com/api/leagues?id=42", # Champions League
            "https://www.fotmob.com/api/leagues?id=73", # Europa League
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




finished_games = []
error_list = []

i = 1
for link in url_list:
    res = requests.get(link)
    jasondata = res.json()

    for match in jasondata['matches']['allMatches']:
        try:
            game_id = match['id']
            finished = match['status']['finished']
            cancelled = match['status']['cancelled']

            query = f"SELECT * FROM Games WHERE match_id = {game_id}"
            in_database = call_db(query)

            if finished and not cancelled and not in_database:
                finished_games.append(game_id)

        except KeyError:
            pass

    print("Getting League:",i,"/",len(url_list))
    i = i + 1

i = 1

for game_id in finished_games:

    try:
        get_starter_stats(game_id)
        get_bench_stats(game_id)
    except:
        pass

    try:
        try:
            game_url = start_game_url + str(game_id)
            fot_res = requests.get(game_url)
            jasondata = fot_res.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching game data for ID {game_id}: {e}")

        
        

        stats = {}
                    
        match_id = jasondata['general']['matchId']
        date = jasondata['general']['matchTimeUTCDate'].split("T")[0]
        League = jasondata['general']['parentLeagueName']
        Country = jasondata['general']['countryCode']
        HomeTeam = jasondata['general']['homeTeam']['name'].replace("'"," ")
        AwayTeam = jasondata['general']['awayTeam']['name'].replace("'"," ")
        HGoals = jasondata['header']['teams'][0]['score']
        AGoals = jasondata['header']['teams'][1]['score']

        insert_league_query = f"""
            INSERT INTO Leagues (League, Nation)
            SELECT '{League}', '{Country}'
            WHERE NOT EXISTS (SELECT League FROM Leagues WHERE League = '{League}')
        """
        call_db(insert_league_query)

        insert_team_query = f"""
            INSERT INTO Teams (Team)
            SELECT '{HomeTeam}'
            WHERE NOT EXISTS (SELECT Team FROM Teams WHERE Team = '{HomeTeam}')
        """
        call_db(insert_team_query)

        insert_team_query = f"""
            INSERT INTO Teams (Team)
            SELECT '{AwayTeam}'
            WHERE NOT EXISTS (SELECT Team FROM Teams WHERE Team = '{AwayTeam}')
        """
        call_db(insert_team_query)


        
        for i in range(0,100):
            for j in range(0, 100):
                try:
                    stat_name = jasondata['content']['stats']['Periods']['All']['stats'][i]['stats'][j]['key']
                    home_stat = jasondata['content']['stats']['Periods']['All']['stats'][i]['stats'][j]['stats'][0]
                    away_stat = jasondata['content']['stats']['Periods']['All']['stats'][i]['stats'][j]['stats'][1]

                    stats["Home" + stat_name.replace(" ","")] = home_stat
                    stats["Away" + stat_name.replace(" ","")] = away_stat
                except:
                    pass
        
        try:
            HomexG = stats['Homeexpected_goals']
        except:
            HomexG = "NULL"

        try:
            AwayxG = stats['Awayexpected_goals']
        except:
            AwayxG = "NULL"

        try:
            HomePoss = stats['HomeBallPossesion']
        except:
            HomePoss = "NULL"

        try:
            AwayPoss = stats['AwayBallPossesion']
        except:
            AwayPoss = "NULL"

        try:
            HomeShots = stats['Hometotal_shots']
        except:
            HomeShots = "NULL"

        try:
            AwayShots = stats['Awaytotal_shots']
        except:
            AwayShots = "NULL"

        try:
            HomeSonT = stats['HomeShotsOnTarget']
        except:
            HomeSonT = "NULL"

        try:
            AwaySonT = stats['AwayShotsOnTarget']
        except:
            AwaySonT = "NULL"

        try:
            HomeSoffT = stats['HomeShotsOffTarget']
        except:
            HomeSoffT = "NULL"

        try:
            AwaySoffT = stats['AwayShotsOffTarget']
        except:
            AwaySoffT = "NULL"

        try:
            HomeBS = stats['Homeblocked_shots']
        except:
            HomeBS = "NULL"

        try:
            AwayBS = stats['Awayblocked_shots']
        except:
            AwayBS = "NULL"

        try:
            HomeCor = stats['Homecorners']
        except:
            HomeCor = "NULL"

        try:
            AwayCor = stats['Awaycorners']
        except:
            AwayCor = "NULL"

        try:
            HomeOff = stats['HomeOffsides']
        except:
            HomeOff = "NULL"

        try:
            AwayOff = stats['AwayOffsides']
        except:
            AwayOff = "NULL"

        try:
            HomeFoul = stats['Homefouls']
        except:
            HomeFoul = "NULL"

        try:
            AwayFoul = stats['Awayfouls']
        except:
            AwayFoul = "NULL"

        try:
            HomeYellow = stats['Homeyellow_cards']
        except:
            HomeYellow = "NULL"

        try:
            AwayYellow = stats['Awayyellow_cards']
        except:
            AwayYellow = "NULL"

        try:
            HomeRed = stats['Homered_cards']
        except:
            HomeRed = "NULL"

        try:
            AwayRed = stats['Awayred_cards']
        except:
            AwayRed = "NULL"

        try:
            HomePass = stats['Homepasses']
        except:
            HomePass = "NULL"

        try:
            AwayPass = stats['Awaypasses']
        except:
            AwayPass = "NULL"

        try:
            HomeAccPass = stats['Homeaccurate_passes'].split(" ")[0]
        except:
            HomeAccPass = "NULL"

        try:
            AwayAccPass = stats['Awayaccurate_passes'].split(" ")[0]
        except:
            AwayAccPass = "NULL"

        try:
            HomePassOff = stats['Homeopposition_half_passes']
        except:
            HomePassOff = "NULL"

        try:
            AwayPassOff = stats['Awayopposition_half_passes']
        except:
            AwayPassOff = "NULL"

        try:
            HomeAccLongB = stats['Homelong_balls_accurate'].split(" ")[0]
        except:
            HomeAccLongB = "NULL"

        try:
            AwayAccLongB = stats['Awaylong_balls_accurate'].split(" ")[0]
        except:
            AwayAccLongB = "NULL"

        try:
            HomeAccLongBpercent = stats['Homelong_balls_accurate'].split(" ")[1].replace("%","").replace("(","").replace(")","")
        except:
            HomeAccLongBpercent = "NULL"

        try:
            AwayAccLongBpercent = stats['Awaylong_balls_accurate'].split(" ")[1].replace("%","").replace("(","").replace(")","")
        except:
            AwayAccLongBpercent = "NULL"

        try:
            HomeAccCross = stats['Homeaccurate_crosses'].split(" ")[0]
        except:
            HomeAccCross = "NULL"

        try:
            AwayAccCross = stats['Awayaccurate_crosses'].split(" ")[0]
        except:
            AwayAccCross = "NULL"

        try:
            HomeAccCrosspercent = stats['Homeaccurate_crosses'].split(" ")[1].replace("%","").replace("(","").replace(")","")
        except:
            HomeAccCrosspercent = "NULL"

        try:
            AwayAccCrosspercent = stats['Awayaccurate_crosses'].split(" ")[1].replace("%","").replace("(","").replace(")","")
        except:
            AwayAccCrosspercent = "NULL"

        try:
            HomeSuccDribb = stats['Homedribbles_succeeded'].split(" ")[0]
        except:
            HomeSuccDribb = "NULL"

        try:
            AwaySuccDribb = stats['Awaydribbles_succeeded'].split(" ")[0]
        except:
            AwaySuccDribb = "NULL"

        try:
            HomeSuccDribbpercent = stats['Homedribbles_succeeded'].split(" ")[1].replace("%","").replace("(","").replace(")","")
        except:
            HomeSuccDribbpercent = "NULL"

        try:
            AwaySuccDribbpercent = stats['Awaydribbles_succeeded'].split(" ")[1].replace("%","").replace("(","").replace(")","")
        except:
            AwaySuccDribbpercent = "NULL"

        try:
            HomeDuelsW = stats['Homeduel_won']
        except:
            HomeDuelsW = "NULL"

        try:
            AwayDuelsW = stats['Awayduel_won']
        except:
            AwayDuelsW = "NULL"

        try:
            HomeTackW = stats['Hometackles_succeeded'].split(" ")[0]
        except:
            HomeTackW = "NULL"

        try:
            AwayTackW = stats['Awaytackles_succeeded'].split(" ")[0]
        except:
            AwayTackW = "NULL"
        
        try:
            HomeTackWpercent = stats['Hometackles_succeeded'].split(" ")[1].replace("%","").replace("(","").replace(")","")
        except:
            HomeTackWpercent = "NULL"

        try:
            AwayTackWpercent = stats['Awaytackles_succeeded'].split(" ")[1].replace("%","").replace("(","").replace(")","")
        except:
            AwayTackWpercent = "NULL"

        try:
            HomeInt = stats['Homeinterceptions']
        except:
            HomeInt = "NULL"

        try:
            AwayInt = stats['Awayinterceptions']
        except:
            AwayInt = "NULL"

        try:
            HomeClear = stats['Homeclearances']
        except:
            HomeClear = "NULL"

        try:
            AwayClear = stats['Awayclearances']
        except:
            AwayClear = "NULL"


        query = f"""
            INSERT INTO Games (match_id, date, League, Country, HomeTeam, AwayTeam, HGoals, AGoals, HomexG, AwayxG, HomePoss, AwayPoss, HomeShots, AwayShots, HomeSonT, AwaySonT, HomeSoffT, AwaySoffT, HomeBS, AwayBS, HomeCor, AwayCor, HomeOff, AwayOff, HomeFoul, AwayFoul, HomeYellow, AwayYellow, HomeRed, AwayRed, HomePass, AwayPass, HomeAccPass, AwayAccPass, HomePassOff, AwayPassOff, HomeAccLongB, AwayAccLongB, HomeAccLongBpercent, AwayAccLongBpercent, HomeAccCross, AwayAccCross, HomeAccCrosspercent, AwayAccCrosspercent, HomeSuccDribb, AwaySuccDribb, HomeSuccDribbpercent, AwaySuccDribbpercent, HomeDuelsW, AwayDuelsW, HomeTackW, AwayTackW, HomeTackWpercent, AwayTackWpercent, HomeInt, AwayInt, HomeClear, AwayClear)
            VALUES ({match_id}, '{date}', '{League}', '{Country}', '{HomeTeam}', '{AwayTeam}', {HGoals}, {AGoals}, {HomexG}, {AwayxG}, {HomePoss}, {AwayPoss}, {HomeShots}, {AwayShots}, {HomeSonT}, {AwaySonT}, {HomeSoffT}, {AwaySoffT}, {HomeBS}, {AwayBS}, {HomeCor}, {AwayCor}, {HomeOff}, {AwayOff}, {HomeFoul}, {AwayFoul}, {HomeYellow}, {AwayYellow}, {HomeRed}, {AwayRed}, {HomePass}, {AwayPass}, {HomeAccPass}, {AwayAccPass}, {HomePassOff}, {AwayPassOff}, {HomeAccLongB}, {AwayAccLongB}, {HomeAccLongBpercent}, {AwayAccLongBpercent}, {HomeAccCross}, {AwayAccCross}, {HomeAccCrosspercent}, {AwayAccCrosspercent}, {HomeSuccDribb}, {AwaySuccDribb}, {HomeSuccDribbpercent}, {AwaySuccDribbpercent}, {HomeDuelsW}, {AwayDuelsW}, {HomeTackW}, {AwayTackW}, {HomeTackWpercent}, {AwayTackWpercent}, {HomeInt}, {AwayInt}, {HomeClear}, {AwayClear})
        """

        call_db(query)
        print(date, HomeTeam, AwayTeam)
        print(finished_games.index(game_id), "/" ,len(finished_games))
    except:
        print("Was not found!")
        error_list.append(game_id)


  