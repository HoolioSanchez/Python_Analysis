import requests
from apps import apps 
from credentials import creds
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class DataRequest: 
    def __init__(self, allData, fdata):
        self.allData = allData
        self.fData = fdata

    def filterLibringData(self, rawdata):
        print('DATA being filtered...')
        for index in rawdata['connections']:
            self.allData.append(index)
            for app in apps: 
                if index['app'] == app:
                    self.fData.append(index)
        print('Data filter complete...')

    def getLibringData(self, startDate, endDate):
        url = 'https://api.libring.com/v2/reporting/get'

        headers = {
            'Authorization': 'Token ' + creds['libring'],
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
        self.filterLibringData(data)

    def getSheetsData(self, data):
        config = 'ads-dashboard-09a9acd8430f.json'
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(config, scope)
        gc = gspread.authorize(credentials)
        wks = gc.open('(YTD) Apps Run Rate').sheet1

        data = wks.get_all_records()

        return data

