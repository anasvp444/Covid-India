# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:54:23 2020

@author: User
"""

import csv
import requests
CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSc_2y5N0I67wDU38DjDh35IZSIS30rQf7_NYZhtYYGU1jJYT6_kDx4YpF-qw0LSlGsBYP8pqM_a1Pd/pub?output=csv&gid=1278947571'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)   
 
import pandas as pd
import numpy as np
df = pd.DataFrame(np.array(my_list))    
headers = df.iloc[0]
df  = pd.DataFrame(df.values[1:], columns=headers)
df = df.set_index('State')
cleanData = df.replace(to_replace='', value=np.nan)
cleanData = cleanData[cleanData['Total_Tested'].notna()]
cleanData = cleanData[cleanData['Positive'].notna()]
cleanData = cleanData[cleanData['Negative'].notna()]


ax = cleanData.iloc[:-1,0:3].astype(float).plot(kind='bar',figsize=(20,14));
ax.set_title("StateWise Tested Numbers Data", fontsize=18)
fig = ax.get_figure()
fig.savefig('StateWise Tested Numbers Data.jpg')


