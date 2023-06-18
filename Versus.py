import matplotlib.pyplot as plt
import pandas as pd
import pymannkendall as mk
class GHG:
    def __init__(self,region,ppl):
        self.region = region
        self.ppl = ppl
        self.data = pd.read_csv('Greenhouse_Gas.csv')
        self.data = self.data.loc[self.data['Country/Region']==region]
        self.data = self.data.loc[self.data['Gas_Type']=='Greenhouse gas']
        # self.data.info()
    def sum(self):
        self.temp = self.data.drop(columns= ['ObjectId2','Country/Region','ISO2','ISO3','Indicator','Unit','Source','CTS_Code','CTS_Name','CTS_Full_Descriptor','Industry','Gas_Type','Scale'],axis = 1)
        # self.temp.info()
        ghg = []
        column = self.temp.columns
        for c in column:
            ghg.append(self.temp[c].sum()/self.ppl)
        return ghg
westeurope = GHG('Western Europe',5)
europeY = westeurope.sum()
westasia = GHG('Western Asia',14)
asiaY = westasia.sum()
x = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
plt.plot(x,europeY,label='Western Europe')
plt.plot(x,asiaY,label='Western Asia')
plt.legend()
plt.show()
# 趋势分析模型
europe = mk.original_test(europeY,0.5)
print("西欧地区温室气体排放量变化趋势:")
print(europe)
asia = mk.original_test(asiaY,0.5)
print("西呀地区温室气体排放量变化趋势:")
print(asia)


