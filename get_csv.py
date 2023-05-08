import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import sqlite3


conn = sqlite3.connect('MatchDB.db')
# Load the data into a pandas dataframe
df = pd.read_sql('SELECT * FROM Games', conn)

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Get the active worksheet
worksheet = workbook.active

# Write the header row to the worksheet
header = list(df.columns)
worksheet.append(header)

# Write the data rows to the worksheet
for r in dataframe_to_rows(df, index=False, header=False):
    worksheet.append(r)

# Save the workbook to a file
workbook.save('games.xlsx')

conn.close()