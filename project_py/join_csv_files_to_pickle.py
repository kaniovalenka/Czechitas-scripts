# join csv files to one csv file by Lenka

import pandas as pd
import os 
import pickle

DATA_PATH = r"C:\Users\lenka\Documents\data analýza\DA\PROJEKT\Hovory\zakl pandas\2024_01_03"

filenames = os.listdir(DATA_PATH)
 

filenames_cdr = []
filenames_cmr = []
for filename in filenames:
    if filename[:3] == 'cdr':
        filenames_cdr.append(filename)
    elif filename[:3] == 'cmr':
        filenames_cmr.append(filename)


cdr_dataframes = []
for filename in filenames_cdr:
    file_path = DATA_PATH + '\\' + filename
    df = pd.read_csv(file_path, header=[0,1])
    cdr_dataframes.append(df)

cdr_joined_df = pd.concat(cdr_dataframes)

with open('all_cdr_files_in_one.pkl', 'wb') as f:
    pickle.dump(cdr_joined_df, f)


cmr_dataframes = []
for filename in filenames_cmr:
    file_path = DATA_PATH + '\\' + filename
    df = pd.read_csv(file_path, header=[0,1])
    cmr_dataframes.append(df)

cmr_joined_df = pd.concat(cmr_dataframes)

with open('all_cmr_files_in_one.pkl', 'wb') as f:
    pickle.dump(cmr_joined_df, f)