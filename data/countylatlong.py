# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:52:31 2020

@author: kgite
"""
#newdf.isna().sum()

#newdf.drop(['stationnum','time','wcode','herb_green','shrub_green','season','solar_rad','winddir_peakgust','speed_peakgust'])


import pandas as pd
import re
import requests as r
import time

a = pd.read_csv("firesCA.csv")



respmatch = r'<County FIPS="(\d+)" name="([A-Za-z\s]+)"/>'

codes = []
names=[]

for i in range(len(a.index)):
    if pd.isnull(a.iloc[i]["COUNTY"]):
        lat = a.iloc[i]["LATITUDE"]
        long = a.iloc[i]["LONGITUDE"]
        url = f"https://geo.fcc.gov/api/census/block/find?latitude={lat}&longitude={long}&format=xml"
        response = r.get(url)
        #print(response.text)
        county=re.findall(respmatch, response.text)[0]
        #print(county)
        codes.append(county[0])
        names.append(county[1])
        time.sleep(.05)
    else:
        codes.append(a.iloc[i]["FIPS_CODE"])
        names.append(a.iloc[i]["FIPS_NAME"])
    #print(i)
        

a["FIPS_NAME"] = names
a["FIPS_CODE"] = codes


a.to_csv("firesCA.csv")
a.iloc[:50].to_csv("firesCA_small.csv")



"""
a['DATE'] = pd.to_datetime(a['DISCOVERY_DATE'] - pd.Timestamp(0).to_julian_date(), unit='D')
a['MONTH'] = pd.DatetimeIndex(a['DATE']).month
a["date"] = pd.to_datetime(a["date"],format="%Y%m%d")
Split counties, convert fips code to float
"""


