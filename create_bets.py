import pandas as pd

df = pd.read_excel("odds.xlsx")



df2 = pd.DataFrame({
    'Date': pd.Series(dtype='str'),
    'League': pd.Series(dtype='str'),
    'Country': pd.Series(dtype='str'),
    'HomeTeam': pd.Series(dtype='str'),
    'AwayTeam': pd.Series(dtype='str'),
    'Bet': pd.Series(dtype='str'),
    'Bettype': pd.Series(dtype='str'),
    'Odds': pd.Series(dtype='float'),
    'FairOdds': pd.Series(dtype='float'),
    'Value': pd.Series(dtype='float'),
    
})

df.loc[(df['HomeOdds'] / df['fairHomeOdds']) > 1.05, 'BetHome'] = 'True' 
df.loc[(df['DrawOdds'] / df['fairDrawOdds']) > 1.05, 'BetDraw'] = 'True' 
df.loc[(df['AwayOdds'] / df['fairAwayOdds']) > 1.05, 'BetAway'] = 'True' 
df.loc[(df['OverOdds'] / df['fairOverOdds']) > 1.05, 'BetOver'] = 'True' 
df.loc[(df['UnderOdds'] / df['fairUnderOdds']) > 1.05, 'BetUnder'] = 'True' 
df.loc[(df['BTTSOdds'] / df['fairBTTSOdds']) > 1.05, 'BetBTTS'] = 'True' 
df.loc[(df['nBTTSOdds'] / df['fairnBTTSOdds']) > 1.05, 'BetnBTTS'] = 'True' 



home_df = df.copy()

home_df = home_df.dropna(subset=['BetHome'])

home_df['Bet'] = '1'

home_df = home_df[['Date', 'League', 'Country', 'HomeTeam','AwayTeam', 'Bet', 'HomeOdds', 'fairHomeOdds']]

home_df.rename(columns={"HomeOdds": "Odds"}, inplace=True)
home_df.rename(columns={"fairHomeOdds": "fairOdds"}, inplace=True)



############################

away_df = df.copy()

away_df = away_df.dropna(subset=['BetAway'])

away_df['Bet'] = '2'

away_df = away_df[['Date', 'League', 'Country', 'HomeTeam','AwayTeam', 'Bet', 'AwayOdds', 'fairAwayOdds']]

away_df.rename(columns={"AwayOdds": "Odds"}, inplace=True)
away_df.rename(columns={"fairAwayOdds": "fairOdds"}, inplace=True)



############################

over_df = df.copy()

over_df = over_df.dropna(subset=['BetOver'])

over_df['Bet'] = 'Over'

over_df = over_df[['Date', 'League', 'Country', 'HomeTeam','AwayTeam', 'Bet', 'OverOdds', 'fairOverOdds']]

over_df.rename(columns={"OverOdds": "Odds"}, inplace=True)
over_df.rename(columns={"fairOverOdds": "fairOdds"}, inplace=True)


############################

under_df = df.copy()

under_df = under_df.dropna(subset=['BetUnder'])

under_df['Bet'] = 'Under'

under_df = under_df[['Date', 'League', 'Country', 'HomeTeam','AwayTeam', 'Bet', 'UnderOdds', 'fairUnderOdds']]

under_df.rename(columns={"UnderOdds": "Odds"}, inplace=True)
under_df.rename(columns={"fairUnderOdds": "fairOdds"}, inplace=True)

############################

btts_df = df.copy()

btts_df = btts_df.dropna(subset=['BetBTTS'])

btts_df['Bet'] = 'BTTS'

btts_df = btts_df[['Date', 'League', 'Country', 'HomeTeam','AwayTeam', 'Bet', 'BTTSOdds', 'fairBTTSOdds']]

btts_df.rename(columns={"BTTSOdds": "Odds"}, inplace=True)
btts_df.rename(columns={"fairBTTSOdds": "fairOdds"}, inplace=True)



############################

nbtts_df = df.copy()

nbtts_df = nbtts_df.dropna(subset=['BetnBTTS'])

nbtts_df['Bet'] = 'nBTTS'

nbtts_df = nbtts_df[['Date', 'League', 'Country', 'HomeTeam','AwayTeam', 'Bet', 'nBTTSOdds', 'fairnBTTSOdds']]

nbtts_df.rename(columns={"nBTTSOdds": "Odds"}, inplace=True)
nbtts_df.rename(columns={"fairnBTTSOdds": "fairOdds"}, inplace=True)

############################

all_df = pd.concat([home_df, away_df, over_df, under_df, btts_df, nbtts_df])

# all_df = all_df[['Date', 'League', 'Country', 'HomeTeam','AwayTeam', 'Bet', 'Odds', 'fairOdds']]

all_df = all_df.sort_values(['League','HomeTeam'])



all_df.to_csv("bets.csv", index=False)

