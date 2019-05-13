#%%
import numpy as np
import pandas as pd 
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import rcParams
#%%
rcParams['figure.figsize'] = 20,5
sb.set_style('white')

#%%
ironsourceCsvFile = 'Performance_Report_per_app_2018-12-1_2019-5-5.csv'
soomlaCsvFile = 'export (18).csv'
dau_csvFile = 'export (17).csv'

df = pd.DataFrame.from_csv(ironsourceCsvFile)
soomlaDF = pd.DataFrame.from_csv(soomlaCsvFile)
dauDF = pd.DataFrame.from_csv(dau_csvFile)

soomlaDF = soomlaDF.sort_index()
soomlaDF.head()

#%%

date = []
d = 0
while d < len(dauDF.index):
    date.append(d)
    d += 1

xtickMarks = [0, 25, 50, 100, 125, 150]

plt.plot(date,dauDF['DAU'], label = 'DAU')
plt.xticks(xtickMarks)
plt.show()
# dauDF.plot()
#%%
jan = df.loc['2019-01-01':'2019-02-04']
jDAU = dauDF.loc['2019-01-01':'2019-02-04']

april = df.loc['2019-04-01':'2019-05-05']
aDAU = dauDF.loc['2019-04-01':'2019-05-05']

competitiorAds = soomlaDF.loc['2019-04-01': '2019-05-05']

jDAU = jDAU.sort_index()
aDAU = aDAU.sort_index()
#%%
competitiorAds.head()
#%%
janTotalRevenue = jan['Revenue'].groupby(['Date']).sum()
jan_eCPM = jan['eCPM'].groupby(['Date']).mean()
jan_impressions = jan['Impressions'].groupby(['Date']).sum()
jan_DAU = jDAU['DAU']
jan_ARPDAU  = janTotalRevenue / jan_DAU

jan_main = pd.DataFrame()
jan_main['Revenue'] = janTotalRevenue
jan_main['eCPM'] = jan_eCPM
jan_main['impressions'] = jan_impressions
jan_main['DAU'] = jan_DAU
jan_main['ARPDAU'] = jan_ARPDAU

jan_main.head() 
#%%
aprilTotalRevenue = april['Revenue'].groupby(['Date']).sum()
april_eCPM = april['eCPM'].groupby(['Date']).mean()
april_impressions = april['Impressions'].groupby(['Date']).sum()
april_DAU = aDAU['DAU']
april_ARPDAU  = aprilTotalRevenue / april_DAU

april_main = pd.DataFrame()
april_main['Revenue'] = aprilTotalRevenue
april_main['eCPM'] = april_eCPM
april_main['impressions'] = april_impressions
april_main['DAU'] = april_DAU
april_main['ARPDAU'] = april_ARPDAU

april_main.head() 

#%%

competitiorAds_rev = competitiorAds['CompRev']
competitiorAds_avgRev = competitiorAds_rev.mean()
competitiorAds_impressions = competitiorAds['Comp_Impressions']
competitiorAds_eCPM = competitiorAds['Comp_eCPM']
competitiorAds_ARPDAU = competitiorAds_rev / april_DAU

comp_ads = pd.DataFrame()
comp_ads['Revenue'] = competitiorAds_rev
comp_ads['impressions'] = competitiorAds_impressions
comp_ads['eCPM'] = competitiorAds_eCPM
comp_ads['ARPDAU'] = competitiorAds_ARPDAU

comp_ads.head()
#%%
days = []
day = 0
while day < len(janTotalRevenue.index):
    days.append(day)
    day += 1
print(days)

# Revenue Graph
#%%
plt.plot(days, aprilTotalRevenue, label = 'April Total Revenue', color = 'darkolivegreen')
plt.plot(days, competitiorAds_rev, label = 'Competitor Ads Revenue', color = 'red')
plt.plot(days, janTotalRevenue, label = ' Total Non Competitor Revenue', color = 'slategrey')
plt.legend()
plt.show()



#%%
janTemp1 = jan_main.reset_index()
aprilTemp1 = april_main.reset_index()
compTemp1 = comp_ads.reset_index()

totalDF = pd.DataFrame(days)
# REVENUE
totalDF['Jan Total Revenue'] = janTemp1['Revenue']
totalDF['April Total Revenue'] = aprilTemp1['Revenue']
totalDF['Delta Revenue'] = (aprilTemp1['Revenue']-janTemp1['Revenue'])/janTemp1['Revenue']
totalDF['Competitor Ads Revenue'] = compTemp1['Revenue']

# DAU
totalDF['Jan DAU'] = janTemp1['DAU']
totalDF['April DAU'] = aprilTemp1['DAU']
totalDF['Delt DAU'] = (aprilTemp1['DAU']-janTemp1['DAU'])/janTemp1['DAU']

#ARPDAU
totalDF['Jan ARPDAU'] = janTemp1['ARPDAU']
totalDF['April ARPDAU'] = aprilTemp1['ARPDAU']
totalDF['Delta ARPDAU'] = (aprilTemp1['ARPDAU']-janTemp1['ARPDAU'])/janTemp1['ARPDAU']
totalDF['Comp ARPDAU'] = compTemp1['ARPDAU']
totalDF['Delta Comp ARPDAU'] = (compTemp1['ARPDAU']-janTemp1['ARPDAU'])/janTemp1['ARPDAU']
#eCPMs
totalDF['Jan eCPM'] = janTemp1['eCPM']
totalDF['April eCPM'] = aprilTemp1['eCPM']
totalDF['Delta eCPM'] = (aprilTemp1['eCPM'] - janTemp1['eCPM'])/janTemp1['eCPM']
totalDF['Comp eCPM'] = compTemp1['eCPM']
totalDF['Delta Comp eCPM'] = (compTemp1['eCPM'] - janTemp1['eCPM'])/janTemp1['eCPM']
totalDF.head()

#Impressions
totalDF['Jan Impressions'] = janTemp1['impressions']
totalDF['April Impressions'] = aprilTemp1['impressions']
totalDF['Delta Impressions'] = (aprilTemp1['impressions'] - janTemp1['impressions'])/janTemp1['impressions']
totalDF['Comp Impressions'] = compTemp1['impressions']

totalDF.to_csv('FG_CompAds_v2.csv')
