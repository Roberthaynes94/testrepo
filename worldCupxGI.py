# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:16:50 2022

@author: rober
"""

import pandas as pd

stuff = pd.read_csv('2022-2023 Football Player Stats_copy.csv',sep=',',encoding='latin1')

epl14 = pd.read_csv('Understat/Understat xG 14.csv')
epl15 = pd.read_csv('Understat/Understat xG 15.csv')
epl16 = pd.read_csv('Understat/Understat xG 16.csv')
epl17 = pd.read_csv('Understat/Understat xG 17.csv')
epl18 = pd.read_csv('Understat/Understat xG 18.csv')
epl19 = pd.read_csv('Understat/Understat xG 19.csv')
epl20 = pd.read_csv('Understat/Understat xG 20.csv')
epl21 = pd.read_csv('Understat/Understat xG 21.csv')
epl22 = pd.read_csv('Understat/Understat xG 22.csv')

buli22 = pd.read_csv('Understat/Understat xG buli 22.csv')
buli21 = pd.read_csv('Understat/Understat xG buli 21.csv')
buli20 = pd.read_csv('Understat/Understat xG buli 20.csv')
buli19 = pd.read_csv('Understat/Understat xG buli 19.csv')
buli18 = pd.read_csv('Understat/Understat xG buli 18.csv')
buli17 = pd.read_csv('Understat/Understat xG buli 17.csv')
buli16 = pd.read_csv('Understat/Understat xG buli 16.csv')
buli15 = pd.read_csv('Understat/Understat xG buli 15.csv')
buli14 = pd.read_csv('Understat/Understat xG buli 14.csv')

lali22 = pd.read_csv('Understat/Understat xG lali 22.csv')
lali21 = pd.read_csv('Understat/Understat xG lali 21.csv')
lali20 = pd.read_csv('Understat/Understat xG lali 20.csv')
lali19 = pd.read_csv('Understat/Understat xG lali 19.csv')
lali18 = pd.read_csv('Understat/Understat xG lali 18.csv')
lali17 = pd.read_csv('Understat/Understat xG lali 17.csv')
lali16 = pd.read_csv('Understat/Understat xG lali 16.csv')
lali15 = pd.read_csv('Understat/Understat xG lali 15.csv')
lali14 = pd.read_csv('Understat/Understat xG lali 14.csv')

sa22 = pd.read_csv('Understat/Understat xG sa 22.csv')
sa21 = pd.read_csv('Understat/Understat xG sa 21.csv')
sa20 = pd.read_csv('Understat/Understat xG sa 20.csv')
sa19 = pd.read_csv('Understat/Understat xG sa 19.csv')
sa18 = pd.read_csv('Understat/Understat xG sa 18.csv')
sa17 = pd.read_csv('Understat/Understat xG sa 17.csv')
sa16 = pd.read_csv('Understat/Understat xG sa 16.csv')
sa15 = pd.read_csv('Understat/Understat xG sa 15.csv')
sa14 = pd.read_csv('Understat/Understat xG sa 14.csv')

lu22 = pd.read_csv('Understat/Understat xG lu 22.csv')
lu21 = pd.read_csv('Understat/Understat xG lu 21.csv')
lu20 = pd.read_csv('Understat/Understat xG lu 20.csv')
lu19 = pd.read_csv('Understat/Understat xG lu 19.csv')
lu18 = pd.read_csv('Understat/Understat xG lu 18.csv')
lu17 = pd.read_csv('Understat/Understat xG lu 17.csv')
lu16 = pd.read_csv('Understat/Understat xG lu 16.csv')
lu15 = pd.read_csv('Understat/Understat xG lu 15.csv')
lu14 = pd.read_csv('Understat/Understat xG lu 14.csv')

league_year_list = [epl21, epl20, epl19, epl18, epl17, epl16, epl15, epl14,
                    buli21, buli20, buli19, buli18, buli17, buli16, buli15, buli14,
                    lali21, lali20, lali19, lali18, lali17, lali16, lali15, lali14,
                    sa21, sa20, sa19, sa18, sa17, sa16, sa15, sa14,
                    lu21, lu20, lu19, lu18, lu17, lu16, lu15, lu14]
LY_suffix_list = ['_21', '_20', '_19', '_18', '_17', '_16', '_15', '_14',
                  '_b21', '_b20', '_b19', '_b18', '_b17', '_b16', '_b15', '_b14',
                  '_l21', '_l20', '_l19', '_l18', '_l17', '_l16', '_l15', '_l14',
                  '_s21', '_s20', '_s19', '_s18', '_s17', '_s16', '_s15', '_s14',
                  '_f21', '_f20', '_f19', '_f18', '_f17', '_f16', '_f15', '_f14']
y = 0

players = pd.concat([epl22, buli22, lali22, sa22, lu22])
players = players.drop_duplicates(subset=['id'])

players = players[['id', 'player_name', 'time', 'goals', 'xG', 'assists', 'xA']]

for x in league_year_list:
    players = players.merge(x[['id','player_name', 'time', 'goals', 'xG', 'assists', 'xA']],
        on = ['id', 'player_name'], how = 'left', suffixes=('', LY_suffix_list[y]))
    y = y+1
    
#%%
xG_columns = ['xG', 'xG_21', 'xG_20', 'xG_19', 'xG_18', 'xG_17', 'xG_16', 'xG_15', 'xG_14',
              'xG_b21', 'xG_b20', 'xG_b19', 'xG_b18', 'xG_b17', 'xG_b16', 'xG_b15', 'xG_b14',
              'xG_l21', 'xG_l20', 'xG_l19', 'xG_l18', 'xG_l17', 'xG_l16', 'xG_l15', 'xG_l14',
              'xG_s21', 'xG_s20', 'xG_s19', 'xG_s18', 'xG_s17', 'xG_s16', 'xG_s15', 'xG_s14',
              'xG_f21', 'xG_f20', 'xG_f19', 'xG_f18', 'xG_f17', 'xG_f16', 'xG_f15', 'xG_f14']
xA_columns = ['xA', 'xA_21', 'xA_20', 'xA_19', 'xA_18', 'xA_17', 'xA_16', 'xA_15', 'xA_14',
              'xA_b21', 'xA_b20', 'xA_b19', 'xA_b18', 'xA_b17', 'xA_b16', 'xA_b15', 'xA_b14',
              'xA_l21', 'xA_l20', 'xA_l19', 'xA_l18', 'xA_l17', 'xA_l16', 'xA_l15', 'xA_l14',
              'xA_s21', 'xA_s20', 'xA_s19', 'xA_s18', 'xA_s17', 'xA_s16', 'xA_s15', 'xA_s14',
              'xA_f21', 'xA_f20', 'xA_f19', 'xA_f18', 'xA_f17', 'xA_f16', 'xA_f15', 'xA_f14']
goals_columns = ['goals', 'goals_21', 'goals_20', 'goals_19', 'goals_18', 'goals_17',
                 'goals_16', 'goals_15', 'goals_14',
                 'goals_b21', 'goals_b20', 'goals_b19', 'goals_b18', 'goals_b17', 'goals_b16',
                 'goals_b15', 'goals_b14',
                 'goals_l21', 'goals_l20', 'goals_l19', 'goals_l18', 'goals_l17', 'goals_l16',
                 'goals_l15', 'goals_l14',
                 'goals_s21', 'goals_s20', 'goals_s19', 'goals_s18', 'goals_s17', 'goals_s16',
                 'goals_s15', 'goals_s14',
                 'goals_f21', 'goals_f20', 'goals_f19', 'goals_f18', 'goals_f17', 'goals_f16',
                 'goals_f15', 'goals_f14']
assists_columns = ['assists', 'assists_21', 'assists_20', 'assists_19', 'assists_18',
              'assists_17', 'assists_16', 'assists_15', 'assists_14',
              'assists_b21', 'assists_b20', 'assists_b19', 'assists_b18', 'assists_b17',
              'assists_b16', 'assists_b15', 'assists_b14',
              'assists_l21', 'assists_l20', 'assists_l19', 'assists_l18', 'assists_l17',
              'assists_l16', 'assists_l15', 'assists_l14',
              'assists_s21', 'assists_s20', 'assists_s19', 'assists_s18', 'assists_s17',
              'assists_s16', 'assists_s15', 'assists_s14',
              'assists_f21', 'assists_f20', 'assists_f19', 'assists_f18', 'assists_f17',
              'assists_f16', 'assists_f15', 'assists_f14']
time_columns = ['time', 'time_21', 'time_20', 'time_19', 'time_18', 'time_17', 'time_16',
                'time_15', 'time_14',
                'time_b21', 'time_b20', 'time_b19', 'time_b18', 'time_b17', 'time_b16',
                'time_b15', 'time_b14',
                'time_l21', 'time_l20', 'time_l19', 'time_l18', 'time_l17', 'time_l16',
                'time_l15', 'time_l14',
                'time_s21', 'time_s20', 'time_s19', 'time_s18', 'time_s17', 'time_s16',
                'time_s15', 'time_s14',
                'time_f21', 'time_f20', 'time_f19', 'time_f18', 'time_f17', 'time_f16',
                'time_f15', 'time_f14']

players['time_tot'] = players[time_columns].sum(axis=1)
players['goals_tot'] = players[goals_columns].sum(axis=1)
players['xG_tot'] = players[xG_columns].sum(axis=1)
players['assists_tot'] = players[assists_columns].sum(axis=1)
players['xA_tot'] = players[xA_columns].sum(axis=1)

# 2022/23, 2021/22 and 2020/21 seasons only
players['time_2'] = players[['time', 'time_21', 'time_20', 'time_b21', 'time_b20', 'time_l21', 'time_l20',
                     'time_s21', 'time_s20','time_f21', 'time_f20']].sum(axis=1)
players['goals_2'] = players[['goals', 'goals_21', 'goals_20', 'goals_b21', 'goals_b20', 'goals_l21', 'goals_l20',
                      'goals_s21', 'goals_s20', 'goals_f21', 'goals_f20']].sum(axis=1)
players['xG_2'] = players[['xG', 'xG_21', 'xG_20', 'xG_b21', 'xG_b20', 'xG_l21', 'xG_l20', 'xG_s21', 'xG_s20',
                      'xG_f21', 'xG_f20']].sum(axis=1)
players['assists_2'] = players[['assists', 'assists_21', 'assists_20', 'assists_b21', 'assists_b20', 'assists_l21', 'assists_l20',
                        'assists_s21', 'assists_s20', 'assists_f21', 'assists_f20']].sum(axis=1)
players['xA_2'] = players[['xA', 'xA_21', 'xA_20', 'xA_b21', 'xA_b20', 'xA_l21', 'xA_l20', 'xA_s21', 'xA_s20',
                        'xA_f21', 'xA_f20']].sum(axis=1)


players = players[players['time_tot'] > 3000]

xGI_columns = ['xG_tot', 'xA_tot']
xGI_columns2 = ['xG_2', 'xA_2']

xGI_and_GI_columns = ['xG_tot', 'xA_tot', 'goals_tot', 'assists_tot']
xGI_and_GI_columns2 = ['goals_2', 'xG_2', 'assists_2', 'xA_2']

players['xGI/90'] = (90*players[xGI_columns].sum(axis=1))/players['time_tot']
players['xGI/90_last3'] = (90*players[xGI_columns2].sum(axis=1))/players['time_2']

players['xGI+GI/90'] = (90*players[xGI_and_GI_columns].sum(axis=1))/players['time_tot']
players['xGI+GI/90_last3'] = ((90*players[xGI_and_GI_columns2].sum(axis=1))/players['time_2'])
players['xGI+GI/90_delta'] = ((90*players[xGI_and_GI_columns2].sum(axis=1))/players['time_2']) - players['xGI+GI/90']
players.loc[players['time_2'] < 1000, 'xGI+GI/90_delta'] = players.loc[players['time_2'] < 1000, 'xGI+GI/90_delta'] * 0

players_tot = players[['player_name','time_tot', 'goals_tot', 'xG_tot', 'assists_tot',
               'xA_tot', 'xGI/90', 'goals_2', 'xG_2', 'assists_2', 'xA_2',
                'time_2', 'xGI/90_last3']]

#players_tot = players[['player_name','time_tot', 'goals_tot', 'xG_tot', 'assists_tot',
#               'xA_tot', 'xGI/90', 'xGI+GI/90', 'goals_2', 'xG_2', 'assists_2', 'xA_2',
#                'time_2', 'xGI/90_last3', 'xGI+GI/90_delta', 'xGI+GI/90_last3']]

# %%

stuff.rename(columns = {'Player':'player_name'}, inplace = True)
stuff = stuff.drop_duplicates(subset=['player_name'])
stuff2 = stuff[['player_name','Nation','Pos','Squad','Age','Min']]

players_tot2 = players_tot.merge(stuff2,how = 'left')
players_tot2 = players_tot2.dropna()

countries = ['ARG','BEL','BRA','CMR','CAN','CRO','DEN','ECU','ENG','FRA','GER',
             'GHA','JPN','MEX','MAR','NED','POL','POR','RSA','SEN','SRB','KOR',
             'ESP','SUI','TUN','USA','URU','WAL']

worldcup = players_tot2[players_tot2.Nation.isin(countries)]








worldcup.to_csv(index=False, path_or_buf = 'Understat/worldcup.csv')
