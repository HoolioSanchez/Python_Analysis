#%%
import pandas as pd
from apps import apps
import matplotlib.pyplot as plt

class Graph:
    def plotAppsLineGraph(self, rawDataFrame, revString, appString, total = None):

        for app in apps: 
            appDF = rawDataFrame[rawDataFrame[appString] == app]
            plt.plot(appDF.index, appDF[revString], label = app, linewidth = 3.3)

        if total != None:
            plt.plot(appDF.index, total(rawDataFrame[revString]), label = 'Total Sum', linewidth = 3.3)
        
        plt.title('Ad Revenue')
        plt.xlabel('Date')
        plt.ylabel('Revenue')
        daterange = ['2019-04-01', '2019-04-05','2019-04-10', '2019-04-15','2019-04-20', '20190-04-23']
        plt.xticks(daterange)
        plt.legend()
        plt.savefig('Ad_Revenue.png')
        plt.show()

    def plotAppsPieGraph(self, rawDataFrame):

        for app in apps: 
            appDF = rawDataFrame[rawDataFrame['app'] == app]
            plt.plot(appDF.index, appDF['ad_revenue'], label = app, linewidth = 3.3)
        
        # plt.plot(appDF.index, totalDailySum(rawDataFrame), label = 'Total Sum', linewidth = 3.3)
        plt.title('Ad Revenue')
        plt.xlabel('Date')
        plt.ylabel('Revenue')
        daterange = ['2019-04-01', '2019-04-05','2019-04-10', '2019-04-15','2019-04-20', '20190-04-23']
        plt.xticks(daterange)
        plt.legend()
        plt.savefig('Ad_Revenue.png')
        plt.show()

