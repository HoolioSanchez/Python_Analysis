#%%
from dataRequest import DataRequest
from apps import apps
from graph import Graph
from google import Gsheets
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import datetime as datetime
from apps import apps 
import seaborn as sb 
from matplotlib import rcParams

#%%
rcParams['figure.figsize'] = 15,10
sb.set_style('whitegrid')

graph = Graph()
x_label = 'Date'
y_label = 'Ad Revenue'
adRevMonthDailyGoal = 121549

#raw data 
rawData = []
filterData = []
sheetsData = []

#%% - LIBRING DATA:
dr = DataRequest(rawData, filterData)
# dr.getLibringData('2019-04-01', '2019-04-30')

#%% - GOOGLE DATA:
googleData = dr.getSheetsData(sheetsData)
gDF = pd.DataFrame(googleData)
gDF.dtypes

gDF['Date'] = pd.to_datetime(gDF['Date'])
gDF.dtypes

#%%
gDF = gDF.set_index('Date')
gDF.head()
#%%
aprilData = gDF.loc['2019-04-01': '2019-04-30']
marchData = gDF.loc['2019-03-01': '2019-03-31']
#%%
aprilData.head()
# marchData.head()

#%%
revCol = 'Ad Revenue ($)'
appCol = 'App'
aprilRevData = aprilData[[appCol, revCol]]

graph.plotAppsLineGraph(aprilRevData, 'Ad Rev', 'Date', 'Rev', revCol, appCol)

#%%
def getARPDAU(dataFrame, appList, revList, breakDownParameter):
    results = pd.DataFrame()
    totalRev = dataFrame[revList].resample(breakDownParameter).mean()
    avgDAU = dataFrame['DAU'].resample(breakDownParameter).mean()
    arpdau = totalRev/avgDAU

    results['ARPDAU'] = arpdau
    return results

#%%
def getAllARPDAU(dataframe, appList, revList, breakdown):
    results = pd.DataFrame()
    appendDF = pd.DataFrame()

    for app in apps: 
        tempDF = dataframe[dataframe[appList] == app]
        arpdau = getARPDAU(tempDF, appList, revList, breakdown)
        appendDF = arpdau
        appendDF['App Name'] = app

        results = results.append(appendDF)

    return results
#%%

apirlARPDAU = getAllARPDAU(aprilData, appCol, revCol, 'w')
allDF = getAllARPDAU(gDF, appCol, revCol, 'M')

allDF.head()
#%%
def getGrowthARPDAU(dataframe,presentSet, perviousSet):
    # (present  - pervious) / pervious X 100 
    #results = ((presentSet - perviousSet) / perviousSet) * 100
    results = pd.DataFrame()

    for app in apps: 
            tempDF = dataframe[dataframe['App Name'] == app]
            tempDF.reset_index()
            print(tempDF)
    
    return results

#%%

def getRateOfChange(dataframe):
        results = pd.DataFrame()
        for app in apps: 
                tempDF = dataframe[dataframe['App Name'] == app]
                appDF = tempDF
                appDF['RateOfChange'] = tempDF['ARPDAU'].pct_change()
                appDF['App Name'] = app
                results = results.append(appDF)

        return results

def getRevData(dataframe, appList, revList, breakDownParameter):
        results = pd.DataFrame()
        totalRev = dataframe[revList].resample(breakDownParameter).sum()
        results['Total Rev'] = totalRev
        return results

#%%
aprilRate = getRateOfChange(apirlARPDAU)
allRate = getRateOfChange(allDF)
allRate.head(20)
# aprilRate.to_csv('rateChange.csv')

#%%
def getAllRevData(dataframe, appList, revList, breakDownParameter):
        results = pd.DataFrame()
        for app in apps: 
                temp = dataframe[dataframe[appList] == app]
                totalAdRev = getRevData(temp, appList, revList, breakDownParameter)
                appendDF = totalAdRev
                appendDF['App'] = app
                results = results.append(appendDF)
        return results 

#%%
allRevData = gDF[[revCol, appCol]]

totalAppRev = allRevData[revCol].resample('m').sum()
totalAppRev2 = getAllRevData(allRevData, appCol, revCol, 'm')
totalAppRev2.to_csv('Month Rev.csv')
