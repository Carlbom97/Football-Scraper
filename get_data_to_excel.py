import sqlite3
import pandas as pd

conn = sqlite3.connect('MatchDB.db')
df = pd.read_sql_query("SELECT * FROM Games", conn)

df.to_excel("data.xlsx", index=False)