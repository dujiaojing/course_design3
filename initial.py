from pylab import *                                 #支持中文
from sklearn.preprocessing import StandardScaler,normalize
import pandas as pd


plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
mpl.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内


data1 = pd.read_csv('D:\hejingshujuji\landscape temperature\Temp.csv')
data2 = pd.read_csv('D:\hejingshujuji\energy transition\Energy_Transition.csv')
# print(data2)


# 温度增量
x1 = []
ydata = []
y1 = data1.loc[[223],'F1961':'F2021'].values.tolist()
y1 = list(itertools.chain.from_iterable(y1)) # 将其转化为一维列表
for i in range(1,len(y1),1):
    ydata.append(float(y1[i])-float(y1[i-1]))
# print(ydata)
for i in range(1962,2022,1):
    x1.append(i)
plt.plot(x1, ydata, color='red',  linewidth=1.2, mec='r', mfc='w', label=u'temperature increment')
plt.legend()
plt.show()

# 温度
x2 = []
# print(y1)
for i in range(1961,2022,1):
    x2.append(i)
# print(x2)
plt.plot(x2, y1, color='red',  linewidth=1.2, mec='r', mfc='w', label=u'temperature')
plt.legend()
plt.show()

data_1 = data1.loc[[223],'F2000':'F2020'].values.tolist() # 将dataframe转为list类型
# 对数据进行归一化处理
data_1 = np.array(data_1) # 变成一维矩阵
data_1 = data_1.reshape(1,-1) # 变成二维矩阵
data_1 = normalize(data_1,axis=1,norm='max')[0] # 归一化后再提取出一维矩阵

data_2 = data2.loc[[2535],'F2000':'F2020'].values.tolist()
data_2 = np.array(data_2)
data_2 = data_2.reshape(1,-1)
data_2 = normalize(data_2,axis=1,norm='max')[0]

data_3 = data2.loc[[2537],'F2000':'F2020'].values.tolist()
data_3 = np.array(data_3)
data_3 = data_3.reshape(1,-1)
data_3 = normalize(data_3,axis=1,norm='max')[0]

data_4 = data2.loc[[2539],'F2000':'F2020'].values.tolist()
data_4 = np.array(data_4)
data_4 = data_4.reshape(1,-1)
data_4 = normalize(data_4,axis=1,norm='max')[0]

data_5 = data2.loc[[2541],'F2000':'F2020'].values.tolist()
data_5 = np.array(data_5)
data_5 = data_5.reshape(1,-1)
data_5 = normalize(data_5,axis=1,norm='max')[0]

data_6 = data2.loc[[2543],'F2000':'F2020'].values.tolist()
data_6 = np.array(data_6)
data_6 = data_6.reshape(1,-1)
data_6 = normalize(data_6,axis=1,norm='max')[0]

data_7 = data2.loc[[2545],'F2000':'F2020'].values.tolist()
data_7 = np.array(data_7)
data_7 = data_7.reshape(1,-1)
data_7 = normalize(data_7,axis=1,norm='max')[0]

data_8 = data2.loc[[2547],'F2000':'F2020'].values.tolist()
data_8 = np.array(data_8)
data_8 = data_8.reshape(1,-1)
data_8 = normalize(data_8,axis=1,norm='max')[0]

data_9 = data2.loc[[2549],'F2000':'F2020'].values.tolist()
data_9 = np.array(data_9)
data_9 = data_9.reshape(1,-1)
data_9 = normalize(data_9,axis=1,norm='max')[0]

data_10 = data2.loc[[2551],'F2000':'F2020'].values.tolist()
data_10 = np.array(data_10)
data_10 = data_10.reshape(1,-1)
data_10 = normalize(data_10,axis=1,norm='max')[0]

data_11 = data2.loc[[2553],'F2000':'F2020'].values.tolist()
data_11 = np.array(data_11)
data_11 = data_11.reshape(1,-1)
data_11 = normalize(data_11,axis=1,norm='max')[0]
xdata = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]



plt.plot(xdata, data_1, color='red',  linewidth=1.2, mec='r', mfc='w', label=u'temperature')
plt.plot(xdata, data_2, color='blue',  linewidth=1.2, mec='r', mfc='w', label=u'Bioenergy')
plt.plot(xdata, data_4, color='green',  linewidth=1.2, mec='r', mfc='w', label=u'Geothermal energy')
plt.plot(xdata, data_5, color='black',  linewidth=1.2, mec='r', mfc='w', label=u'Hydropower')
plt.plot(xdata, data_6, color='magenta',  linewidth=1.2, mec='r', mfc='w', label=u'Marine energy')
plt.plot(xdata, data_10, color='pink',  linewidth=1.2, mec='r', mfc='w', label=u'Solar energy')
plt.plot(xdata, data_11, color='purple',  linewidth=1.2, mec='r', mfc='w', label=u'Wind energy')
plt.legend()
plt.xlabel(u'x-data', size=12)
plt.ylabel(u'y-data', size=12)

plt.show()

plt.plot(xdata, data_1, color='red',  linewidth=1.2, mec='r', mfc='w', label=u'temperature')
plt.plot(xdata, data_3, color='cyan',  linewidth=1.2, mec='r', mfc='w', label=u'Fossil fuels')
plt.plot(xdata, data_7, color='yellow',  linewidth=1.2, mec='r', mfc='w', label=u'Nuclear')
plt.plot(xdata, data_8, color='orange',  linewidth=1.2, mec='r', mfc='w', label=u'Other non-renewable energy')
plt.plot(xdata, data_9, color='olive',  linewidth=1.2, mec='r', mfc='w', label=u'Pumped storage')
plt.legend()
plt.xlabel(u'x-data', size=12)
plt.ylabel(u'y-data', size=12)

plt.show()

# 温度的方差
data = data1.loc[(data1['Country/Region'] == 'World'),'F1961':'F2020'].values.tolist()
data = list(itertools.chain.from_iterable(data))
print(data)

def Variance(start,end):
    sum1 = 0
    sum2 = 0
    for i in range(start,end+1):
        sum1 += data[i]
    average = sum1/(end-start+1)
    for i in range(start,end+1):
        sum2 += pow(abs(data[i]-average),2)
    variance = sum2/(end-start+1)
    return average,variance
list1 = []
list1.append(Variance(0,19))
list1.append(Variance(20,39))
list1.append(Variance(40,59))
print(list1)





