# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:29:21 2021

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:29:21 2021

@author: JIN_HUSSEIN
"""
'''
# Location based replacement
df.loc[2,'ST_NUM'] = 125
'''
import pandas as pd 
data = pd.read_csv("country_vaccination_stats.csv")
data = data[["country", "date", "daily_vaccinations", "vaccines"]]
countries = data['country']
a = countries[0]
index = 0
baslangic = 1
for i in countries:
    if (i == a ):
        index = index +1
    else:
        a = i
        if(not ( data[baslangic-1:index]['daily_vaccinations'].isnull().all())):
            minvalue =  data[baslangic-1:index]['daily_vaccinations'].min()
            data[baslangic-1:index]['daily_vaccinations'].fillna(minvalue, inplace = True)
        else:
            data[baslangic-1:index]['daily_vaccinations'].fillna(0, inplace = True)
        baslangic = index+1
        index = index +1
        
        
if(not ( data[baslangic-1:index]['daily_vaccinations'].isnull().all())):
    
    minvalue =  data[baslangic-1:index]['daily_vaccinations'].min()
    data[baslangic-1:index]['daily_vaccinations'].fillna(minvalue, inplace = True)
else:
    
    data[baslangic-1:index]['daily_vaccinations'].fillna(0, inplace = True)

data.to_csv('country_vaccination_stats1.csv')


