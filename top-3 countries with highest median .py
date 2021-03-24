import pandas as pd 
data = pd.read_csv("country_vaccination_stats.csv")
data = data[["country", "date", "daily_vaccinations", "vaccines"]]
countries = data['country']
a = countries[0]
index = 0
baslangic = 1
medianlist = []
for i in countries:
    if (i == a ):
        index = index +1
    else: 
        if(not ( data[baslangic-1:index]['daily_vaccinations'].isnull().all())):
            data[baslangic-1:index]['daily_vaccinations'].fillna(0, inplace = True) ##filling all the nan values with 0's 
            data[baslangic-1:index].sort_values(by=['daily_vaccinations']) #sorting the values 
            median = data[baslangic-1:index]['daily_vaccinations'].median()
            templist = [median,a]
            medianlist.append(templist)
        else:
            data[baslangic-1:index]['daily_vaccinations'].fillna(0, inplace = True)
            templist = [0,a]
            medianlist.append(templist)
        baslangic = index+1
        index = index +1
        a = i
        
if(not ( data[baslangic-1:index]['daily_vaccinations'].isnull().all())):
    data[baslangic-1:index]['daily_vaccinations'].fillna(0, inplace = True) ##filling all the nan values with 0's 
    data[baslangic-1:index].sort_values(by=['daily_vaccinations']) #sorting the values 
    median = data[baslangic-1:index]['daily_vaccinations'].median()
    templist = [median,a]
    medianlist.append(templist)
else:
    data[baslangic-1:index]['daily_vaccinations'].fillna(0, inplace = True)
    templist =[0,a]
    medianlist.append(templist) 
highestmedian = sorted(zip(medianlist), reverse=True)[:3]
print(highestmedian[0][0][1] )
print(highestmedian[1][0][1] )
print( highestmedian[2][0][1] )
    