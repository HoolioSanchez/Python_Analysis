import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apps import apps

#GOOGLE SHEETS - connection 
config = 'ads-dashboard-09a9acd8430f.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(config, scope)
gc = gspread.authorize(credentials)
wks = gc.open('(YTD) Apps Run Rate').sheet1

#Fliter apps/metric
def addRowToSheets(data):
    wks.append_row(data, value_input_option='USER_ENTERED')

def filterDataRows(index) :
    row = [index['date'], index['app'], index['impressions'], index['ad_revenue'], index['dau'], index['clicks'],index['conversions']]
    return row

def appendFilterApps(data):
    for index in data['connections']:
        for app in apps:
            if index['app'] == app:
                rows = filterDataRows(index)
                addRowToSheets(rows)
    print('Complete')
