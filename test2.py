from db import call_db
import requests

url_list = ["https://www.fotmob.com/api/leagues?id=47",
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
            "https://www.fotmob.com/api/leagues?id=64"
            ]

league_games = []

for link in url_list:

    res = requests.get(link)
    jasondata = res.json()

    for table_data in jasondata['table']:
        League = table_data['data']['leagueName']
        try:
            Country = table_data['data']['ccode']
        except KeyError:
            Country = 'Unknown'

    query = f"SELECT COUNT(id) FROM Games WHERE League = '{League}'"

    data = call_db(query)

    string = League,"|",data

    league_games.append(string)

for row in league_games:
    print(row)