from player2 import *
import sqlite3
import re

conn = sqlite3.connect("MatchDB.db")
cursor = conn.cursor()
query = "SELECT match_id FROM GAMES"
cursor.execute(query)
rows = cursor.fetchall()
numbers = []
for row in rows:
    match = re.search(r'\d+', str(row))
    if match:
        numbers.append(int(match.group()))
conn.close()

numbers = numbers[4788:]

start = 1

for game in numbers:
    try:
        get_starter_stats(game)
        get_bench_stats(game)
        print(start,"/",len(numbers))
        start += 1
    except:
        print("Error Game:",game,"/",len(numbers))
        start += 1