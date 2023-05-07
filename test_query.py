from db import call_db, get_value
from regression import stats_list, home_stats_list, away_stats_list, get_coefficients

query = "SELECT Count(AwayTeam) FROM Games WHERE AwayTeam = 'Millwall'"
query2 = "SELECT AVG(AwaySonT) FROM Games WHERE HomeTeam = 'Luton Town'"


result = call_db(query)
result2 = call_db(query2)

print(result, result2)