from apps import apps

#GOOGLE SHEETS - Fliter apps/metric

class Gsheets: 
    def __init__(self, wks): 
        self.wks = wks

    def appendFilterApps(self, data):
        for index in data['connections']:
            for app in apps:
                if index['app'] == app:
                    rows = self.filterDataRows(index)
                    self.addRowToSheets(rows)
        print('EVENT: Complete')

    def addRowToSheets(self, data):
        self.wks.append_row(data, value_input_option='USER_ENTERED')

    def filterDataRows(self, index) :
        row = [index['date'], index['app'], index['impressions'], index['ad_revenue'], index['dau'], index['clicks'],index['conversions']]
        return row
