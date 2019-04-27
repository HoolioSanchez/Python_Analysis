#%%
from dataRequest import DataRequest
from apps import apps
from graph import Graph
from google import Gsheets
import pandas as pd 
import matplotlib as plt

#%%
rawData = []
filterData = []
sheetsData = []

#Getting Data
dr = DataRequest(rawData, filterData)
dr.getLibringData('2019-04-01', '2019-04-05')
googleData = dr.getSheetsData(sheetsData)

#%%
gDF = pd.DataFrame(googleData)
gDF.index = gDF['Date']

#%%
def totalDailySum(rawDataFrame, revString):
    tempDf = rawDataFrame[revString]
    tempDf.index = pd.to_datetime(tempDf.index)
    total = tempDf.resample('d').sum()
    return total

# def forcastDailySum(rawDataFrame, num):
#     total = totalDailySum(rawDataFrame)
#     count = len(total)
#     average = total / count

#%%
total = totalDailySum(gDF, 'Ad Revenue ($)')

#%%
total.head()

grh = Graph()
grh.plotAppsLineGraph(gDF)