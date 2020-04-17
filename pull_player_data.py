
import pandas as pd
from sqlalchemy import create_engine

# reading in the parsed data to get player lists
dom = pd.read_excel('data/parsed_data.xlsx', sheet_name='dom')
snd = pd.read_excel('data/parsed_data.xlsx', sheet_name='snd')
hp = pd.read_excel('data/parsed_data.xlsx', sheet_name='hardpoint')
dom = dom.iloc[2:, :].drop('Unnamed: 1', axis=1)
snd = snd.iloc[2:, :].drop('Unnamed: 1', axis=1)
hp = hp.iloc[2:, :].drop('Unnamed: 1', axis=1)

player_list = list(set(list(dom.Player) 
                    + list(snd.Player) 
                    + list(hp.Player)))
bench_list =  [x for x in player_list if x[-2:] == '**']
active_players = [x for x in player_list if x not in bench_list]

team_list = list(set(dom.Team))
# getting hardpoint player data a table in the db
hp_data = {}
for x in active_players:
    hp = pd.read_excel('data/CDL 2020 Stats Lab.xlsx', 
                        sheet_name=x, 
                        skiprows=14,
                        usecols='C:S')
    hp.columns = hp.iloc[0, :]
    hp = hp.iloc[1:]
    hp = hp.dropna(thresh=2)
    hp_data[x] = hp
    
hp_df = pd.DataFrame()
for x in hp_data.keys():
    hp_data[x]['Player'] = x
    hp_df = pd.concat([hp_df, hp_data[x]], axis=0)
hp_df.loc[hp_df.Assists == '-', 'Assists'] = '0'
hp_df.Assists.fillna('0', inplace=True)
hp_df.to_sql('player.hp_matches', 
             con=sqlite3.connect('cdl.sqlite3'))

# getting domination player data into a table in the db
dom_data = {}
for x in active_players:
    dom = pd.read_excel('data/CDL 2020 Stats Lab.xlsx', 
                        sheet_name=x, 
                        skiprows=14,
                        usecols='W:AP')
    dom.columns = dom.iloc[0, :]
    dom = dom.iloc[1:]
    dom = dom.dropna(thresh=3)
    dom_data[x] = dom

dom_df = pd.DataFrame()
for x in dom_data.keys():
    dom_data[x]['Player'] = x
    dom_df = pd.concat([dom_df, dom_data[x]], axis=0)
dom_df.loc[dom_df.Assists == '-', 'Assists'] = '0'
dom_df.loc[dom_df.Assists == '-', 'CAPs'] = '0'
dom_df.Assists.fillna('0', inplace=True)
dom_df.to_sql('player.dom_matches', 
             con=sqlite3.connect('cdl.sqlite3'))

# getting snd player data into a table in the db
snd_data = {}
for x in active_players:
    snd = pd.read_excel('data/CDL 2020 Stats Lab.xlsx', 
                        sheet_name=x, 
                        skiprows=14,
                        usecols='AS:BQ')
    snd.columns = snd.iloc[0, :]
    snd = snd.iloc[1:]
    snd = snd.dropna(thresh=2)
    snd_data[x] = snd

snd_df = pd.DataFrame()
for x in snd_data.keys():
    snd_data[x]['Player'] = x
    snd_df = pd.concat([snd_df, snd_data[x]], axis=0)
snd_df.loc[snd_df.Assists == '-', 'Snipes'] = '0'
snd_df.Assists.fillna('0', inplace=True)
snd_df.to_sql('players.snd_matches', 
             con=sqlite3.connect('cdl.sqlite3'))


engine = create_engine('sqlite:////Users/daman/Desktop/cdl/cdl.db')

# snd databse sheet
snd_db = pd.read_excel('data/CDL 2020 Stats Lab.xlsx', 
                    sheet_name='SnD Games Database')
snd_db.dropna(thresh=3).drop(['Unnamed: 0', 'Unnamed: 2'], axis=1).fillna(0)
for x in snd_db.columns:
    snd_db[x] = snd_db[x].replace('-', 0)
snd_db.to_sql('mode.snd', if_exists='replace', con=engine)

# hp database sheet
hp_db = pd.read_excel('data/CDL 2020 Stats Lab.xlsx', 
                    sheet_name='HP Games Database')
hp_db = hp_db.dropna(thresh=3).drop(['HARDPOINT', 'Unnamed: 2'], axis=1).fillna(0)
for x in hp_db.columns:
    hp_db[x] = hp_db[x].replace('-', 0)
hp_db.to_sql('mode.hp', if_exists='replace', con=engine)

# dom database sheet
dom_db = pd.read_excel('data/CDL 2020 Stats Lab.xlsx', 
                    sheet_name='DOM Games Database')
dom_db = dom_db.dropna(thresh=3).drop(['Unnamed: 0', 'Unnamed: 2'], axis=1).fillna(0)
for x in dom_db.columns:
    dom_db[x] = dom_db[x].replace('-', 0)
dom_db.to_sql('mode.dom', if_exists='replace', con=engine)