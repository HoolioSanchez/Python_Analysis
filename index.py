#%%
import requests
import pandas as pd
import json
from credentials import creds
from apps import apps

libringToken = creds['libring']

storeData = []

def getLibringData(startDate, endDate): 
    url = 'https://api.libring.com/v2/reporting/get'
    headers = {
        'Authorization': 'Token ' + libringToken,
        'content-type': 'application/json'
    }
    queryString = {
        'start_date': startDate,
        'end_date': endDate,
        'group_by': 'date,app'
    }

    payload = ''

    response = requests.request('GET', url, params = queryString, headers = headers, data = payload)

    data = response.json()

    print('GETTING DATA:')
    print(data)
    filterLibringData(data)

    return data


def filterLibringData(rawdata):
    for index in rawdata['connections']:
        for app in apps: 
            if index['app'] == app:
                storeData.append(index)
    print('Data filtered...')

data = getLibringData('2019-04-16','2019-04-16')

#%%
mainDataFrame = pd.DataFrame(storeData)

#%%
mainDataFrame.head()
#%%
mh = mainDataFrame[mainDataFrame['app'] == 'Cookie Jam']
mh.head()

