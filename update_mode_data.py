import pandas as pd 
from sqlalchemy import create_engine

def update_mode_xlsx():
    """
    updates mode_db_data.xlsx for each mode with what is
    present in the Mode DB sheets from the CDL Stats Lab
    """
    # snd databse sheet
    snd_db = pd.read_excel('data/CDL 2020 Stats Lab.xlsx', 
                        sheet_name='SnD Games Database')
    snd_db = snd_db.dropna(thresh=3).drop(['Unnamed: 0', 'Unnamed: 2'], axis=1).fillna(0)
    for x in snd_db.columns:
        snd_db[x] = snd_db[x].replace('-', 0)
    snd_db.to_excel('data/mode_db_snd_data.xlsx', sheet_name='snd', index=False)
    # hp database sheet
    hp_db = pd.read_excel('data/CDL 2020 Stats Lab.xlsx', 
                        sheet_name='HP Games Database')
    hp_db = hp_db.dropna(thresh=3).drop(['HARDPOINT', 'Unnamed: 2'], axis=1).fillna(0)
    for x in hp_db.columns:
        hp_db[x] = hp_db[x].replace('-', 0)
    hp_db.to_excel('data/mode_db_hp_data.xlsx', sheet_name='hp', index=False)
    # dom database sheet
    dom_db = pd.read_excel('data/CDL 2020 Stats Lab.xlsx', 
                        sheet_name='DOM Games Database')
    dom_db = dom_db.dropna(thresh=3).drop(['Unnamed: 0', 'Unnamed: 2'], axis=1).fillna(0)
    for x in dom_db.columns:
        dom_db[x] = dom_db[x].replace('-', 0)
    dom_db.to_excel('data/mode_db_dom_data.xlsx', sheet_name='dom', index=False)    
    print('All modes have been udpated to their corresponding sheet.')

if __name__ == "__main__":
    update_mode_xlsx()
