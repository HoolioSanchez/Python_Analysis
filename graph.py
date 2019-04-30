#%%
import pandas as pd
from apps import apps
import matplotlib.pyplot as plt
import seaborn as sb

#%%
class Graph:

    def appendDailyGoal(self, rawDF, dailyGoalNum):
        goalNum = dailyGoalNum
        tempArray = []

        for x in range(len(rawDF)):
            tempArray.append(goalNum)
            x += 1
        
        return tempArray

    def plotRevGoal(self, rawData, dailyGoal, title, xLabel, yLabel): 

        counter = appendDailyGoal(rawData.index, dailyGoal)
        plt.plot(rawData.index, counter, label = 'Daily Goal', linewidth = 1.5, linestyle = '--')
        plt.plot(rawData.index, rawData['total'], label = 'Total Revenue', linewidth = 1.5)

        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend()
        plt.show()

    def plotAppsLineGraph(self, rawDataFrame, title, xLabel, yLabel):
        for app in apps: 
            appDF = rawDataFrame[rawDataFrame['app'] == app]
            plt.plot(appDF.index, appDF['ad_revenue'], label = app, linewidth = 1.5)

        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend()
        plt.show()

    def plotAppsPieGraph(self, rawDataFrame):
        


