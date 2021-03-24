# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 00:09:44 2021

@author: JIN_HUSSEIN
"""
import datetime
import pandas as pd 
'''
using the dataset that i produced from the 4th question 
'''
data = pd.read_csv("country_vaccination_stats1.csv")
data = data[["country", "date", "daily_vaccinations", "vaccines"]]
dates = data['date']
daily_vaccinations_ = data['daily_vaccinations']
d1 = datetime.datetime(2021, 1, 6)
count = 0
sum_ = 0
for i in dates:
    d2 = datetime.datetime(int(i.split('/')[2]), int(i.split('/')[0]), int(i.split('/')[1]))
    if(d1 == d2):
        if( not(pd.isnull(daily_vaccinations_.iloc[count] ))):
            print( daily_vaccinations_[count])
            sum_ = sum_ + daily_vaccinations_[count]
    count = count +1
print (sum_)
