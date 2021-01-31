# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:41:55 2020

@author: kgite
"""
import os
import pandas as pd
from statistics import multimode
import statistics

counties = ['017-El Dorado',
 '___-________________________',
 '109-Tuolumne',
 '107-Tulare',
 '019-Fresno',
 '007-Butte',
 '057-Nevada',
 '111-Ventura',
 '113-Yolo',
 '065-Riverside',
 '073-San Diego',
 '045-Mendocino',
 '097-Sonoma',
 '037-Los Angeles',
 '005-Amador',
 '087-Santa Cruz',
 '093-Siskiyou',
 '099-Stanislaus',
 '103-Tehama',
 '047-Merced',
 '033-Lake',
 '021-Glenn',
 '043-Mariposa',
 '003-Alpine',
 '013-Contra Costa',
 '023-Humboldt',
 '081-San Mateo',
 '071-San Bernardino',
 '039-Madera',
 '015-Del Norte',
 '035-Lassen',
 '041-Marin',
 '031-Kings',
 '025-Imperial',
 '029-Kern',
 '027-Inyo',
 '083-Santa Barbara',
 '059-Orange',
 '061-Placer',
 '055-Napa',
 '085-Santa Clara',
 '053-Monterey',
 '049-Modoc',
 '051-Mono',
 '069-San Benito',
 '079-San Luis Obispo',
 '089-Shasta',
 '091-Sierra',
 '105-Trinity',
 '011-Colusa',
 '063-Plumas',
 '001-Alameda',
 '009-Calaveras',
 '115-Yuba']

files = os.listdir("ca_wc/")

files = [file for file in files if file[-4:] == ".csv"]

#read all county files together
newdf = pd.DataFrame()
for county in counties:
    county = ''.join(county.split())
    countydf = pd.DataFrame()
    for file in files:
        #print(county,file)
        if county in file:
            smalldf = pd.read_csv("ca_wc/"+file)
            countydf = pd.concat([countydf,smalldf])
            #print(smalldf)
    
    x=countydf.groupby('date').agg('mean')
    x2=countydf[['date','wetflag','snowflag']].groupby(['date']).agg(lambda x: statistics.multimode(x)[0])
    x['county']=county
        
    newdf = pd.concat([newdf,pd.merge(x,x2,how='inner',on='date')])
    

newdf.to_csv("weather_merged_date.csv")

newdf.iloc[:50].to_csv("weather_merged_date_small.csv")

#aggregate and average/take mode

#newdf.groupby('count').aggregate({'data1': 'min','data2': 'max'})

#see if there are any fuel moistures/greenness info
