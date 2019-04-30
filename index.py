#%%
from dataRequest import DataRequest
from apps import apps
from graph import Graph
from google import Gsheets
import pandas as pd 
import matplotlib.pyplot as plt
import datetime as datetime
from apps import apps 
import seaborn as sb 
from matplotlib import rcParams

#%%
rcParams['figure.figsize'] = 10,10
sb.set_style('whitegrid')

#%%
graph = Graph()
x_label = 'Date'
y_label = 'Ad Revenue'
adRevMonthDailyGoal = 121549

#%%
#Getting Data
rawData = []
filterData = []
sheetsData = []

dr = DataRequest(rawData, filterData)
dr.getLibringData('2019-04-22', '2019-04-28')
# googleData = dr.getSheetsData(sheetsData)

#%%
# gDF = pd.DataFrame(googleData)
# gDF.index = gDF['Date']

libAll = pd.DataFrame(rawData)
libFil = pd.DataFrame(filterData)

libAll.dtypes
#%%
libAll['date'] = pd.to_datetime(libAll['date'])
libAll['ad_revenue'] = pd.to_numeric(libAll['ad_revenue'])

libFil['date'] = pd.to_datetime(libFil['date'])
libFil['ad_revenue'] = pd.to_numeric(libFil['ad_revenue'])

#%% 
#libAll.dtypes
libAll_rev = libAll[['date', 'ad_revenue']]
libAll_rev = libAll_rev.set_index('date')
libAll_rev = libAll_rev.resample('d').sum()

libFil_rev = libFil.groupby(['date', 'app']).sum().reset_index()
libFil_rev = libFil_rev.set_index('date')
#%%
libFil_rev.head(100)
#%%
libAll_rev.head()
libAll_rev.plot()

#%%

dates = ['2019-04-22','2019-04-23','2019-04-24','2019-04-25','2019-04-26','2019-04-27','2019-04-28']
total = libFil_rev['ad_revenue'].resample('d').sum()
libFil_rev['total'] = total

#%%
graph.plotAppsLineGraph(libAll_rev, 'App Rev', x_label, y_label)