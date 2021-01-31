# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 00:18:51 2020

@author: kgite
"""
import pandas as pd

left = pd.read_csv("weather_noNA.csv")
right = pd.read_csv("firesCA_cty.csv")

#right['CONTDATE'] = pd.to_datetime(right['CONT_DATE'] - pd.Timestamp(0).to_julian_date(), unit='D')

right["FIPS_CODE"] = right["FIPS_CODE"] % 6000

merged = pd.merge(left,right,how="inner",left_on=["date","FIPS_CODE"],right_on=["DATE","FIPS_CODE"])


merged.to_csv("fire_weather.csv",index=False)
merged.iloc[:100].to_csv("fire_weather_small.csv",index=False)
