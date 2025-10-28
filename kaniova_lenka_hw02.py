import pandas as pd
import json

data = pd.read_csv('netflix_titles.tsv', sep='\t')

data = data[['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR']]

data = data.rename(columns={'PRIMARYTITLE': 'title',
                            'DIRECTOR': 'directors',
                            'CAST': 'cast',
                            'GENRES': 'genres',
                            'STARTYEAR': 'decade'
                            })

data_list = data.to_dict(orient='records')


columns_lists = ['directors', 'cast', 'genres']

for film in data_list:
    for column in columns_lists:
        if pd.notnull(film[column]):
            film[column] = film[column].replace(', ', ',')
            film[column] = film[column].split(',')
        else:
            film[column] = []


for film in data_list:
    film['decade'] = film['decade'] // 10 * 10


with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(data_list, file, indent=4)