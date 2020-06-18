#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:05:57 2020

@author: Simon
"""


import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)
yesterday = yesterday.strftime('20%y-%m-%d')
list_of_terms = ['Goal','Shot']
master_database = pd.DataFrame([])


Game_ID_List = []
for i in np.arange(2017,2019):
        for j in np.arange(1,1271):
            Game_ID_List.append(f'{i}02{j:04d}')


for game in Game_ID_List:
    url = 'https://statsapi.web.nhl.com/api/v1/game/%s/feed/live' %game
    r = requests.get(url)
    game_data = r.json()

    filtered_game = game_data['liveData']
    game_data.keys()
    filtered_game_01 = filtered_game['plays']['allPlays']
    
    #Create index for dataframe based on number of goals scored
    df_index = np.arange(0,len(filtered_game_01),1)
    names = ['Player','X-Location','Y-Location']

    #Create array to extract the coordinates and the name of the scorer for each goal in the game
    df = pd.DataFrame(index=df_index, columns=names)
    #Create empty array with columns
    df = df.fillna(0)

    for x in df_index:
        if any(word in filtered_game_01[x]['result']['event'] for word in list_of_terms):
            try:
                df.loc[x,'Player'] = filtered_game_01[x]['players'][0]['player']['fullName']
                df.loc[x,'X-Location'] = filtered_game_01[x]['coordinates']['x']
                df.loc[x,'Y-Location'] = filtered_game_01[x]['coordinates']['y']
                df.loc[x,'Team'] = filtered_game_01[x]['team']['triCode']
                df.loc[x,'Period Type'] = filtered_game_01[x]['about']['periodType']
                df.loc[x,'Result'] = filtered_game_01[x]['result']['eventTypeId']
                df.loc[x,'Type'] = filtered_game_01[x]['result']['secondaryType']
                df.loc[x,'Date'] = filtered_game_01[11]['about']['dateTime'][:10]
                
            except:
                pass        
                    
    df = df.dropna(axis=0,how='any')
    master_database = master_database.append(df).reset_index(drop=True)
    print(f'Scrapped game: {game}')












