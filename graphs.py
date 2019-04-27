#%%
import requests
import pandas as pd
import json
from credentials import creds
from apps import apps
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rcParams
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import seaborn as sb
from graph import Graph

#%%
rcParams['figure.figsize'] = 20, 10
sb.set_style('whitegrid')
libringToken = creds['libring']

#Temp Data arrays (to be populated by API GET request)
libringData = []
allLibringData = []
gData = []

#%%

def filterLibringData(rawdata):
    print('DATA being filtered...')
    for index in rawdata['connections']:
        allLibringData.append(index)
        for app in apps: 
            if index['app'] == app:
                libringData.append(index)
    print('Data filter complete...')

def getLibringData(startDate, endDate):
    url = 'https://api.libring.com/v2/reporting/get'

    headers = {
        'Authorization': 'Token ' + libringToken,
        'content-type': 'application/json'
    }
    queryString = {
        'period': 'custom_date',
        'start_date': startDate,
        'end_date': endDate,
        'group_by': 'date,app,connection'
    }

    payload = ''

    response = requests.request('GET', url, params = queryString, headers = headers, data = payload)
    data = response.json()
    print('DATA COLLECTION ENDED')

    filterLibringData(data)

#%%
getLibringData('2019-04-01', '2019-04-23')
print(libringData)

#%%
print(allLibringData)

#%%
def getGoogleData(data): 

    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds['google'], scope)

    gc = gspread.authorize(credentials)

    wks = gc.open("(YTD) Apps Run Rate").sheet1

    data = wks.get_all_values()

    return data

#%%

#%%
dataframe = pd.DataFrame(libringData)

#%%
workingDF = dataframe[['date', 'app', 'ad_revenue', 'impressions']]

workingDF.index = workingDF['date']
workingDF['ad_revenue'] = workingDF['ad_revenue'].astype('float64')
workingDF['impressions'] = workingDF['impressions'].astype('float64')

workingDF.drop(['date'], axis = 1)

#%%
workingDF.head()

#%%


#%%
grh = Graph()

workingDF.head()

#%%
grh.plotAppsLineGraph(workingDF)
# plotLineGraph(workingDF)

#%%
# 1. daily average rev 2.remaining days