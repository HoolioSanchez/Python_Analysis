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
rcParams['figure.figsize'] = 10,10
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

#%%
aprilData.head()

#%%
revCol = 'Ad Revenue ($)'
appCol = 'App'
aprilRevData = aprilData[[appCol, revCol]]

graph.plotAppsLineGraph(aprilRevData, 'Ad Rev', 'Date', 'Rev', revCol, appCol)

#%%
aprilDAU = aprilData[[appCol, revCol, 'DAU']]
aprilDAU['ARPDAU'] = (aprilDAU[revCol] / aprilDAU['DAU'])
aprilDAU.head()

#%%
aprilARPDAU = aprilDAU[[appCol, 'ARPDAU']]
graph.plotAppsLineGraph(aprilARPDAU, 'ARPDAU', 'Date', 'ARPDAU','ARPDAU', appCol)
