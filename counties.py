import os
import re
import shutil
import pandas as pd

mypath = "ca/"

files = os.listdir(mypath)

stations = [file[-10:-4] for file in files if file[-4:]==".txt"]

fw13 = [file for file in files if file[-5:]==".fw13"]

colspecs = [(0,2),(3,8),(9,16),(17,20),(21),(22),(23,25),(26,28),(29,31),(32,34),(35,36),(37,39),(40,42),(43,45),
            (46,48),(49,50),(51,55),(56),(57,58),(59,60),(61),(62),(63),(64,67),(68,70),(71,73),(74)]

widths = [3,6,8,4,1,1,3,3,3,3,2,3,3,3,3,2,5,1,2,2,1,1,1,4,3,3,1]
names = ["w13","stationnum","date","time","obstype","wcode","drybulbtemp","atm_moisture","wind_azimuth","avg_windspeed","fuelmoisture","maxtemp","mintemp","maxhumid","minhumid","precip_duration","precip_amt","wetflag","herb_green","shrub_green","moisture_type","meas_type","season","solar_rad","winddir_peakgust","speed_peakgust","snowflag"]


county_year = {}

for file in fw13:
    print(file)
    #county name
    stationnum = file[2:8]
    with open(f'ca/wlstinv1!{stationnum}.txt','r') as myfile:
        county = (re.findall(r'County: (.*)Lat/Lon' ,myfile.read()))[0].strip()
    
    print(county)
    #date range
    with open("ca/"+file,'r') as myfile:
        lines = myfile.readlines()
        daterange = set([line[9:13] for line in lines if (line[9:13] <= '2015') and (line[9:13] >= '1992') ])
    
    print(daterange)
    #rename
    newfile = pd.read_fwf("ca/"+file,widths = widths,header=None)
    
    newfile.to_csv("ca_wc/"+''.join(county.split())+"_"+file[:-5]+".csv",header=names,index=False)
    
    #shutil.copy("ca/"+file,"ca_wc/"+''.join(county.split())+"_"+file)
    #store date range   
    #print(county in county_year)            
    if county in county_year:
        for yr in daterange:
            county_year[county].add(yr)
    else:
        county_year[county] = set(daterange)
    
print(county_year)
        

        
        
