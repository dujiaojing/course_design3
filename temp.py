import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymannkendall as mk
import itertools
from matplotlib.axis import XTick
from pylab import *                                 #支持中文
from sklearn.preprocessing import StandardScaler,normalize


plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
mpl.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内


# data = pd.read_csv('D:\hejingshujuji\landscape temperature\Temp.csv')

class Temp:
    def __init__(self,country,path):
        self.country = country # 列表
        self.data = pd.read_csv(path)

    def add(self):
        region = self.data.loc[(self.data['Country/Region'] == self.country[0]) | (self.data['Country/Region'] == self.country[1]) | (self.data['Country/Region'] == self.country[2]) | (self.data['Country/Region'] == self.country[3]) | (self.data['Country/Region'] == self.country[4])]
        region.info()
        data0 = region.drop(columns=['ObjectId','ISO2','ISO3','Indicator','Unit','Source','CTS_Code','CTS_Name','CTS_Full_Descriptor'],axis=1)
        data = region.drop(columns=['Country/Region','ObjectId','ISO2','ISO3','Indicator','Unit','Source','CTS_Code','CTS_Name','CTS_Full_Descriptor'],axis=1)
        # 对total_list2中的空缺进行填充处理，沿x轴方向，进行填充，选择后面的值
        data = data.fillna(axis=1,method='bfill')
        data0 = data0.fillna(axis=1,method='bfill')
        # print(data0)
        data = np.array(data).tolist() # 将DataFrame类型转为列表类型
        # print(data)
        list1 = []
        j = 0
        while True:
            sum = 0
            for i in data:
                sum += i[j]
            list1.append(sum/5)
            j = j + 1
            if j>=61:
                break
        return list1

temp1 = Temp(['Saudi Arabia','Iran, Islamic Rep. of','Iraq','Kuwait','United Arab Emirates'],'Temp.csv') # 西亚：沙特，伊朗，伊拉克，科威特，阿联酋，
temp2 = Temp(['United Kingdom','France','Ireland','Netherlands, The','Belgium'],'Temp.csv') # 西欧：英国，法国，爱尔兰，荷兰，比利时
list1 = temp1.add()
list_1 = mk.original_test(list1,0.5)
print(list_1)
list2 = temp2.add()
list_2 = mk.original_test(list2,0.5)
print(list_2)
xdata = []
for i in range(1961,2022):
    xdata.append(i)

plt.plot(xdata, list1, color='red',  linewidth=1.2, mec='r', mfc='w', label=u'Western Asia')
plt.plot(xdata, list2, color='blue',  linewidth=1.2, mec='r', mfc='w', label=u'Western Europe')
plt.legend()
plt.show()
