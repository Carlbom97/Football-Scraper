import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression


stats_list = [
            'HomePoss', 
            # 'AwayPoss',
            'HomeShots',
            'AwayShots',
            'HomeSonT',
            'AwaySonT',
            # 'HomeSoffT',
            # 'AwaySoffT',
            'HomeBS',
            'AwayBS',
            'HomeCor',
            'AwayCor',
            'HomeOff',
            'AwayOff',
            'HomeFoul',
            'AwayFoul',
            # 'HomeYellow',
            # 'AwayYellow',
            # 'HomeRed',
            # 'AwayRed',
            'HomePass',
            'AwayPass',
            'HomeAccPass',
            'AwayAccPass',
            'HomePassOff',
            'AwayPassOff',
            'HomeAccLongB',
            'AwayAccLongB',
            'HomeAccLongBpercent',
            'AwayAccLongBpercent',
            'HomeAccCross',
            'AwayAccCross',
            'HomeAccCrosspercent',
            'AwayAccCrosspercent',
            'HomeSuccDribb',
            'AwaySuccDribb',
            'HomeSuccDribbpercent',
            'AwaySuccDribbpercent',
            'HomeDuelsW',
            'AwayDuelsW',
            'HomeTackW',
            'AwayTackW',
            'HomeTackWpercent',
            'AwayTackWpercent',
            'HomeInt',
            'AwayInt',
            'HomeClear',
            'AwayClear'
            ]

home_stats_list = [
            'HomePoss',
            'HomeShots',
            'HomeSonT',
            # 'HomeSoffT',
            'HomeBS',
            'HomeCor',
            'HomeOff',
            'HomeFoul',
            # 'HomeYellow',
            # 'HomeRed',
            'HomePass',
            'HomeAccPass',
            'HomePassOff',
            'HomeAccLongB',
            'HomeAccLongBpercent',
            'HomeAccCross',
            'HomeAccCrosspercent',
            'HomeSuccDribb',
            'HomeSuccDribbpercent',
            'HomeDuelsW',
            'HomeTackW',
            'HomeTackWpercent',
            'HomeInt',
            'HomeClear'
            ]

away_stats_list = [
            # 'AwayPoss',
            'AwayShots',
            'AwaySonT',
            # 'AwaySoffT',
            'AwayBS',
            'AwayCor',
            'AwayOff',
            'AwayFoul',
            # 'AwayYellow',
            # 'AwayRed',
            'AwayPass',
            'AwayAccPass',
            'AwayPassOff',
            'AwayAccLongB',
            'AwayAccLongBpercent',
            'AwayAccCross',
            'AwayAccCrosspercent',
            'AwaySuccDribb',
            'AwaySuccDribbpercent',
            'AwayDuelsW',
            'AwayTackW',
            'AwayTackWpercent',
            'AwayInt',
            'AwayClear'
            ]

def get_coefficients(League, Country):
    # Step 1: Connect to the database
    conn = sqlite3.connect('MatchDB.db')

    # Step 2: Retrieve the data
    df = pd.read_sql_query(f"SELECT * FROM Games WHERE League = '{League}' AND Country = '{Country}'", conn)

    df = df.drop(['HomexG','AwayxG'], axis= 1)

    df = df.dropna()

    X = df[[
        'HomePoss', 
        # 'AwayPoss',
        'HomeShots',
        # 'AwayShots',
        'HomeSonT',
        # 'AwaySonT',
        # 'HomeSoffT',
        # 'AwaySoffT',
        # 'HomeBS',
        'AwayBS',
        'HomeCor',
        # 'AwayCor',
        'HomeOff',
        # 'AwayOff',
        # 'HomeFoul',
        'AwayFoul',
        # 'HomeYellow',
        # 'AwayYellow',
        # 'HomeRed',
        # 'AwayRed',
        'HomePass',
        # 'AwayPass',
        'HomeAccPass',
        # 'AwayAccPass',
        'HomePassOff',
        # 'AwayPassOff',
        'HomeAccLongB',
        # 'AwayAccLongB',
        'HomeAccLongBpercent',
        # 'AwayAccLongBpercent',
        'HomeAccCross',
        # 'AwayAccCross',
        'HomeAccCrosspercent',
        # 'AwayAccCrosspercent',
        'HomeSuccDribb',
        # 'AwaySuccDribb',
        'HomeSuccDribbpercent',
        # 'AwaySuccDribbpercent',
        'HomeDuelsW',
        'AwayDuelsW',
        # 'HomeTackW',
        'AwayTackW',
        # 'HomeTackWpercent',
        'AwayTackWpercent',
        # 'HomeInt',
        'AwayInt',
        # 'HomeClear',
        'AwayClear'
        ]]
    y = df['HGoals']

    # Step 4: Fit the regression model
    reg_home = LinearRegression().fit(X, y)
    home_intercept = reg_home.intercept_

    # Create a dictionary of coefficients and column names

    home_coeff_dict = {}
    for i, coef in enumerate(reg_home.coef_):
        column_name = X.columns[i]
        if column_name in [
            'HomePoss',
            # 'AwayPoss',
            'HomeShots',
            # 'AwayShots',
            'HomeSonT',
            # 'AwaySonT',
            # 'HomeSoffT',
            # 'AwaySoffT',
            # 'HomeBS',
            'AwayBS',
            'HomeCor',
            # 'AwayCor',
            'HomeOff',
            # 'AwayOff',
            # 'HomeFoul',
            'AwayFoul',
            # 'HomeYellow',
            # 'AwayYellow',
            # 'HomeRed',
            # 'AwayRed',
            'HomePass',
            # 'AwayPass',
            'HomeAccPass',
            # 'AwayAccPass',
            'HomePassOff',
            # 'AwayPassOff',
            'HomeAccLongB',
            # 'AwayAccLongB',
            'HomeAccLongBpercent',
            # 'AwayAccLongBpercent',
            'HomeAccCross',
            # 'AwayAccCross',
            'HomeAccCrosspercent',
            # 'AwayAccCrosspercent',
            'HomeSuccDribb',
            # 'AwaySuccDribb',
            'HomeSuccDribbpercent',
            # 'AwaySuccDribbpercent',
            'HomeDuelsW',
            'AwayDuelsW',
            # 'HomeTackW',
            'AwayTackW',
            # 'HomeTackWpercent',
            'AwayTackWpercent',
            # 'HomeInt',
            'AwayInt',
            # 'HomeClear',
            'AwayClear'
            ]:  # Only include these columns
            home_coeff_dict[column_name] = round(coef, 4)


    X = df[[
        'HomePoss',
        # 'AwayPoss',
        # 'HomeShots',
        'AwayShots',
        # 'HomeSonT',
        'AwaySonT',
        # 'HomeSoffT',
        # 'AwaySoffT',
        'HomeBS',
        # 'AwayBS',
        # 'HomeCor',
        'AwayCor',
        # 'HomeOff',
        'AwayOff',
        'HomeFoul',
        # 'AwayFoul',
        # 'HomeYellow',
        # 'AwayYellow',
        # 'HomeRed',
        # 'AwayRed',
        # 'HomePass',
        'AwayPass',
        # 'HomeAccPass',
        'AwayAccPass',
        # 'HomePassOff',
        'AwayPassOff',
        # 'HomeAccLongB',
        'AwayAccLongB',
        # 'HomeAccLongBpercent',
        'AwayAccLongBpercent',
        # 'HomeAccCross'
        'AwayAccCross',
        # 'HomeAccCrosspercent',
        'AwayAccCrosspercent',
        # 'HomeSuccDribb',
        'AwaySuccDribb',
        # 'HomeSuccDribbpercent',
        'AwaySuccDribbpercent',
        'HomeDuelsW',
        'AwayDuelsW',
        'HomeTackW',
        # 'AwayTackW',
        'HomeTackWpercent',
        # 'AwayTackWpercent',
        'HomeInt',
        # 'AwayInt',
        'HomeClear',
        # 'AwayClear'
        ]]
    y = df['AGoals']

    # Step 4: Fit the regression model
    reg_away = LinearRegression().fit(X, y)
    away_intercept = reg_away.intercept_

    # Create a dictionary of coefficients and column names
    away_coeff_dict = {}
    for i, coef in enumerate(reg_away.coef_):
        column_name = X.columns[i]
        if column_name in [
            'HomePoss', 
            # 'AwayPoss',
            # 'HomeShots',
            'AwayShots',
            # 'HomeSonT',
            'AwaySonT',
            # 'HomeSoffT',
            # 'AwaySoffT',
            'HomeBS',
            # 'AwayBS',
            # 'HomeCor',
            'AwayCor',
            # 'HomeOff',
            'AwayOff',
            'HomeFoul',
            # 'AwayFoul',
            # 'HomeYellow',
            # 'AwayYellow',
            # 'HomeRed',
            # 'AwayRed',
            # 'HomePass',
            'AwayPass',
            # 'HomeAccPass',
            'AwayAccPass',
            # 'HomePassOff',
            'AwayPassOff',
            # 'HomeAccLongB',
            'AwayAccLongB',
            # 'HomeAccLongBpercent',
            'AwayAccLongBpercent',
            # 'HomeAccCross',
            'AwayAccCross',
            # 'HomeAccCrosspercent',
            'AwayAccCrosspercent',
            # 'HomeSuccDribb',
            'AwaySuccDribb',
            # 'HomeSuccDribbpercent',
            'AwaySuccDribbpercent',
            'HomeDuelsW',
            'AwayDuelsW',
            'HomeTackW',
            # 'AwayTackW',
            'HomeTackWpercent',
            # 'AwayTackWpercent',
            'HomeInt',
            # 'AwayInt',
            'HomeClear',
            # 'AwayClear'
            ]:  # Only include these columns
            away_coeff_dict[column_name] = round(coef, 4)

    conn.close()


    return home_coeff_dict, away_coeff_dict, home_intercept, away_intercept




