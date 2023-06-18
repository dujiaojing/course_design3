import numpy as np
import pandas as pd
from pylab import *                                 #支持中文
from sklearn.preprocessing import StandardScaler,normalize
import itertools

def normalize1(list):
    newlist = []
    max = list[0]
    for i in range(1,len(list)):
        if list[i]>max:
            max = list[i]
    min = list[0]
    for i in range(1,len(list)):
        if list[i]<min:
            min = list[i]
    list[0] = (max-list[0])/(max-min)
    list[1] = (list[1]-min)/(max-min)
    list[2] = (list[2]-min)/(max-min)
    return list

def normalize(lists):
    newlists = []
    newlists.append(normalize1(lists[0]))
    newlists.append(normalize1(lists[1]))
    newlists.append(normalize1(lists[2]))
    return newlists

def getE(list):
    sum = 0
    for l in list:
        sum = sum + l
    sum = pow(sum,1/len(list))
    return sum

def getD(dict):
    newdict = {}
    for key in dict:
        dict[key] = normalize(dict[key])
        temp = []
        sum = 0
        for i in range(0,len(dict[key])):
            t = getE(dict[key][i])
            temp.append(t)
            sum = sum + t
        ave = sum/len(temp)
        temp.append(ave)
        newdict[key] = temp
    return newdict
###把字典作为参数传入getD(dict)中,返回值是一个字典，字典的每个键对应一个国家，值为一个列表，列表里四个数据[2010eti,2015eti,2020eti,平均eti]

data = pd.read_csv('D:\hejingshujuji\energy transition\Energy_Transition.csv')
dict = {}

# # 澳大利亚
# list1 = data.loc[(data['Country/Region']=='Australia') & (data['Unit']=='Gigawatt-hours (GWh)') & (data['Technology']=='Fossil fuels'),['F2010','F2015','F2020']] # 化石燃料消耗
# # print(list1)
# list1 = np.array(list1).tolist() # 将DataFrame类型转为列表类型
# list1 = list(itertools.chain.from_iterable(list1)) # 将其转化为一维列表
# # print(list1)
#
# total_list1 = data.loc[(data['Country/Region']=='Australia') & (data['Unit']=='Gigawatt-hours (GWh)'),['F2010','F2015','F2020']]
# # 对total_list1中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
# total_list1 = total_list1.fillna(axis=1,method='ffill')
# # print(total_list1)
# total_list1 = np.array(total_list1).tolist() # 将DataFrame类型转为列表类型
#
# j = 0
# zong_list1 = [] # 总能源消耗
# while True:
#     sum = 0
#     for i in total_list1:
#         sum += i[j]
#     zong_list1.append(sum)
#     j = j + 1
#     if j>=3:
#         break
# # print(zong_list1)
#
# renewable_list1 = data.loc[(data['Country/Region']=='Australia') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Energy_Type']=='Total Renewable'),['F2010','F2015','F2020']]
# # 对total_list1中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
# renewable_list1 = renewable_list1.fillna(axis=1,method='ffill')
# # print(renewable_list1)
# renewable_list1 = np.array(renewable_list1).tolist() # 将DataFrame类型转为列表类型
#
# j = 0
# renew_list1 = [] # 可再生能源
# while True:
#     sum = 0
#     for i in renewable_list1:
#         sum += i[j]
#     renew_list1.append(sum)
#     j = j + 1
#     if j>=3:
#         break
# # print(renew_list1)
#
# # 清洁能源
# clean_list1 = []
# for i in range(0,len(zong_list1),1):
#     sum = zong_list1[i] - list1[i]
#     clean_list1.append(sum)
# # print(clean_list1)
#
# # Australia:[[X1,X2,X3],[X1,X2,X3],[X1,X2,X3]]
# Australia_list1 = [] # 2010
# Australia_list2 = [] # 2015
# Australia_list3 = [] # 2020
#
# Australia_list1.append(list1[0]/zong_list1[0])
# Australia_list1.append(renew_list1[0]/zong_list1[0])
# Australia_list1.append(clean_list1[0]/zong_list1[0])
#
# Australia_list2.append(list1[1]/zong_list1[1])
# Australia_list2.append(renew_list1[1]/zong_list1[1])
# Australia_list2.append(clean_list1[1]/zong_list1[1])
#
# Australia_list3.append(list1[2]/zong_list1[2])
# Australia_list3.append(renew_list1[2]/zong_list1[2])
# Australia_list3.append(clean_list1[2]/zong_list1[2])
# print(Australia_list1)
# print(Australia_list2)
# print(Australia_list3)

# 西欧
list2 = data.loc[(data['Country/Region']=='Western Europe') & (data['Unit']=='Gigawatt-hours (GWh)') & (data['Technology']=='Fossil fuels'),['F2010','F2015','F2020']] # 化石燃料消耗
# print(list2)
list2 = np.array(list2).tolist() # 将DataFrame类型转为列表类型
list2 = list(itertools.chain.from_iterable(list2)) # 将其转化为一维列表
# print(list2)

total_list2 = data.loc[(data['Country/Region']=='Western Europe') & (data['Unit']=='Gigawatt-hours (GWh)'),['F2010','F2015','F2020']]
if total_list2.isnull().values.any():
    # 对total_list2中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    total_list2 = total_list2.fillna(axis=1,method='ffill')
# print(total_list2)
total_list2 = np.array(total_list2).tolist() # 将DataFrame类型转为列表类型

j = 0
zong_list2 = [] # 总能源消耗
while True:
    sum = 0
    for i in total_list2:
        sum += i[j]
    zong_list2.append(sum)
    j = j + 1
    if j>=3:
        break
# print(zong_list2)

renewable_list2 = data.loc[(data['Country/Region']=='Western Europe') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Energy_Type']=='Total Renewable'),['F2010','F2015','F2020']]
if renewable_list2.isnull().values.any():
    # 对total_list2中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    renewable_list2 = renewable_list2.fillna(axis=1,method='ffill')
# print(renewable_list2)
renewable_list2 = np.array(renewable_list2).tolist() # 将DataFrame类型转为列表类型

j = 0
renew_list2 = [] # 可再生能源
while True:
    sum = 0
    for i in renewable_list2:
        sum += i[j]
    renew_list2.append(sum)
    j = j + 1
    if j>=3:
        break
# print(renew_list2)

other_list2 = []
other_list2 = data.loc[(data['Country/Region']=='Western Europe') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Technology']=='Other non-renewable energy'),['F2010','F2015','F2020']]
other_list2 = np.array(other_list2).tolist() # 将DataFrame类型转为列表类型
other_list2 = list(itertools.chain.from_iterable(other_list2)) # 将其转化为一维列表
# print(other_list2)

# 清洁能源
clean_list2 = []
for i in range(0,len(zong_list2),1):
    sum = zong_list2[i] - list2[i] - other_list2[i]
    clean_list2.append(sum)
# print(clean_list2)

# Western Europe:[[X1,X2,X3],[X1,X2,X3],[X1,X2,X3]]
Europe_list1 = [] # 2010
Europe_list2 = [] # 2015
Europe_list3 = [] # 2020

Europe_list1.append(list2[0]/zong_list2[0])
Europe_list1.append(renew_list2[0]/zong_list2[0])
Europe_list1.append(clean_list2[0]/zong_list2[0])

Europe_list2.append(list2[1]/zong_list2[1])
Europe_list2.append(renew_list2[1]/zong_list2[1])
Europe_list2.append(clean_list2[1]/zong_list2[1])

Europe_list3.append(list2[2]/zong_list2[2])
Europe_list3.append(renew_list2[2]/zong_list2[2])
Europe_list3.append(clean_list2[2]/zong_list2[2])
# print(Europe_list1)
# print(Europe_list2)
# print(Europe_list3)

# 北美
list3 = data.loc[(data['Country/Region']=='Northern America') & (data['Unit']=='Gigawatt-hours (GWh)') & (data['Technology']=='Fossil fuels'),['F2010','F2015','F2020']] # 化石燃料消耗
# print(list3)
list3 = np.array(list3).tolist() # 将DataFrame类型转为列表类型
list3 = list(itertools.chain.from_iterable(list3)) # 将其转化为一维列表
# print(list3)

total_list3 = data.loc[(data['Country/Region']=='Northern America') & (data['Unit']=='Gigawatt-hours (GWh)'),['F2010','F2015','F2020']]
if total_list3.isnull().values.any():
    # 对total_list3中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    total_list3 = total_list3.fillna(axis=1,method='ffill')
# print(total_list3)
total_list3 = np.array(total_list3).tolist() # 将DataFrame类型转为列表类型

j = 0
zong_list3 = [] # 总能源消耗
while True:
    sum = 0
    for i in total_list3:
        sum += i[j]
    zong_list3.append(sum)
    j = j + 1
    if j>=3:
        break
# print(zong_list3)

renewable_list3 = data.loc[(data['Country/Region']=='Northern America') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Energy_Type']=='Total Renewable'),['F2010','F2015','F2020']]
if renewable_list3.isnull().values.any():
    # 对total_list3中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    renewable_list3 = renewable_list3.fillna(axis=1,method='ffill')
# print(renewable_list3)
renewable_list3 = np.array(renewable_list3).tolist() # 将DataFrame类型转为列表类型

j = 0
renew_list3 = [] # 可再生能源
while True:
    sum = 0
    for i in renewable_list3:
        sum += i[j]
    renew_list3.append(sum)
    j = j + 1
    if j>=3:
        break
# print(renew_list3)

other_list3 = []
other_list3 = data.loc[(data['Country/Region']=='Northern America') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Technology']=='Other non-renewable energy'),['F2010','F2015','F2020']]
other_list3 = np.array(other_list3).tolist() # 将DataFrame类型转为列表类型
other_list3 = list(itertools.chain.from_iterable(other_list3)) # 将其转化为一维列表
# print(other_list3)

# 清洁能源
clean_list3 = []
for i in range(0,len(zong_list3),1):
    sum = zong_list3[i] - list3[i] - other_list3[i]
    clean_list3.append(sum)
# print(clean_list3)

# Northern America:[[X1,X2,X3],[X1,X2,X3],[X1,X2,X3]]
America_list1 = [] # 2010
America_list2 = [] # 2015
America_list3 = [] # 2020

America_list1.append(list3[0]/zong_list3[0])
America_list1.append(renew_list3[0]/zong_list3[0])
America_list1.append(clean_list3[0]/zong_list3[0])

America_list2.append(list3[1]/zong_list3[1])
America_list2.append(renew_list3[1]/zong_list3[1])
America_list2.append(clean_list3[1]/zong_list3[1])

America_list3.append(list3[2]/zong_list3[2])
America_list3.append(renew_list3[2]/zong_list3[2])
America_list3.append(clean_list3[2]/zong_list3[2])
# print(America_list1)
# print(America_list2)
# print(America_list3)

# 东亚
list4 = data.loc[(data['Country/Region']=='Eastern Asia') & (data['Unit']=='Gigawatt-hours (GWh)') & (data['Technology']=='Fossil fuels'),['F2010','F2015','F2020']] # 化石燃料消耗
# print(list4)
list4 = np.array(list4).tolist() # 将DataFrame类型转为列表类型
list4 = list(itertools.chain.from_iterable(list4)) # 将其转化为一维列表
# print(list4)

total_list4 = data.loc[(data['Country/Region']=='Eastern Asia') & (data['Unit']=='Gigawatt-hours (GWh)'),['F2010','F2015','F2020']]
if total_list4.isnull().values.any():
    # 对total_list4中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    total_list4 = total_list4.fillna(axis=1,method='ffill')
# print(total_list4)
total_list4 = np.array(total_list4).tolist() # 将DataFrame类型转为列表类型

j = 0
zong_list4 = [] # 总能源消耗
while True:
    sum = 0
    for i in total_list4:
        sum += i[j]
    zong_list4.append(sum)
    j = j + 1
    if j>=3:
        break
# print(zong_list4)

renewable_list4 = data.loc[(data['Country/Region']=='Eastern Asia') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Energy_Type']=='Total Renewable'),['F2010','F2015','F2020']]
if renewable_list4.isnull().values.any():
    # 对total_list4中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    renewable_list4 = renewable_list4.fillna(axis=1,method='ffill')
# print(renewable_list4)
renewable_list4 = np.array(renewable_list4).tolist() # 将DataFrame类型转为列表类型

j = 0
renew_list4 = [] # 可再生能源
while True:
    sum = 0
    for i in renewable_list4:
        sum += i[j]
    renew_list4.append(sum)
    j = j + 1
    if j>=3:
        break
# print(renew_list4)

other_list4 = []
other_list4 = data.loc[(data['Country/Region']=='Eastern Asia') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Technology']=='Other non-renewable energy'),['F2010','F2015','F2020']]
other_list4 = np.array(other_list4).tolist() # 将DataFrame类型转为列表类型
other_list4 = list(itertools.chain.from_iterable(other_list4)) # 将其转化为一维列表
# print(other_list4)

# 清洁能源
clean_list4 = []
for i in range(0,len(zong_list4),1):
    sum = zong_list4[i] - list4[i] - other_list4[i]
    clean_list4.append(sum)
# print(clean_list4)

# Eastern Asia:[[X1,X2,X3],[X1,X2,X3],[X1,X2,X3]]
Asia_list1 = [] # 2010
Asia_list2 = [] # 2015
Asia_list3 = [] # 2020

Asia_list1.append(list4[0]/zong_list4[0])
Asia_list1.append(renew_list4[0]/zong_list4[0])
Asia_list1.append(clean_list4[0]/zong_list4[0])

Asia_list2.append(list4[1]/zong_list4[1])
Asia_list2.append(renew_list4[1]/zong_list4[1])
Asia_list2.append(clean_list4[1]/zong_list4[1])

Asia_list3.append(list4[2]/zong_list4[2])
Asia_list3.append(renew_list4[2]/zong_list4[2])
Asia_list3.append(clean_list4[2]/zong_list4[2])
# print(Asia_list1)
# print(Asia_list2)
# print(Asia_list3)


# 非洲
list6 = data.loc[(data['Country/Region']=='Africa') & (data['Unit']=='Gigawatt-hours (GWh)') & (data['Technology']=='Fossil fuels'),['F2010','F2015','F2020']] # 化石燃料消耗
# print(list6)
list6 = np.array(list6).tolist() # 将DataFrame类型转为列表类型
list6 = list(itertools.chain.from_iterable(list6)) # 将其转化为一维列表
# print(list6)

total_list6 = data.loc[(data['Country/Region']=='Africa') & (data['Unit']=='Gigawatt-hours (GWh)'),['F2010','F2015','F2020']]
if total_list6.isnull().values.any():
    # 对total_list6中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    total_list6 = total_list6.fillna(axis=1,method='ffill')
# print(total_list6)
total_list6 = np.array(total_list6).tolist() # 将DataFrame类型转为列表类型

j = 0
zong_list6 = [] # 总能源消耗
while True:
    sum = 0
    for i in total_list6:
        sum += i[j]
    zong_list6.append(sum)
    j = j + 1
    if j>=3:
        break
# print(zong_list6)

renewable_list6 = data.loc[(data['Country/Region']=='Africa') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Energy_Type']=='Total Renewable'),['F2010','F2015','F2020']]
if renewable_list6.isnull().values.any():
    # 对total_list6中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    renewable_list6 = renewable_list6.fillna(axis=1,method='ffill')
# print(renewable_list6)
renewable_list6 = np.array(renewable_list6).tolist() # 将DataFrame类型转为列表类型

j = 0
renew_list6 = [] # 可再生能源
while True:
    sum = 0
    for i in renewable_list6:
        sum += i[j]
    renew_list6.append(sum)
    j = j + 1
    if j>=3:
        break
# print(renew_list6)

other_list6 = []
other_list6 = data.loc[(data['Country/Region']=='Africa') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Technology']=='Other non-renewable energy'),['F2010','F2015','F2020']]
other_list6 = np.array(other_list6).tolist() # 将DataFrame类型转为列表类型
other_list6 = list(itertools.chain.from_iterable(other_list6)) # 将其转化为一维列表
# print(other_list6)

# 清洁能源
clean_list6 = []
for i in range(0,len(zong_list6),1):
    sum = zong_list6[i] - list6[i] - other_list6[i]
    clean_list6.append(sum)
# print(clean_list6)

# Africa:[[X1,X2,X3],[X1,X2,X3],[X1,X2,X3]]
Africa_list1 = [] # 2010
Africa_list2 = [] # 2015
Africa_list3 = [] # 2020

Africa_list1.append(list6[0]/zong_list6[0])
Africa_list1.append(renew_list6[0]/zong_list6[0])
Africa_list1.append(clean_list6[0]/zong_list6[0])

Africa_list2.append(list6[1]/zong_list6[1])
Africa_list2.append(renew_list6[1]/zong_list6[1])
Africa_list2.append(clean_list6[1]/zong_list6[1])

Africa_list3.append(list6[2]/zong_list6[2])
Africa_list3.append(renew_list6[2]/zong_list6[2])
Africa_list3.append(clean_list6[2]/zong_list6[2])
# print(Africa_list1)
# print(Africa_list2)
# print(Africa_list3)

# 西亚
list7 = data.loc[(data['Country/Region']=='Western Asia') & (data['Unit']=='Gigawatt-hours (GWh)') & (data['Technology']=='Fossil fuels'),['F2010','F2015','F2020']] # 化石燃料消耗
# print(list7)
list7 = np.array(list7).tolist() # 将DataFrame类型转为列表类型
list7 = list(itertools.chain.from_iterable(list7)) # 将其转化为一维列表
# print(list7)

total_list7 = data.loc[(data['Country/Region']=='Western Asia') & (data['Unit']=='Gigawatt-hours (GWh)'),['F2010','F2015','F2020']]
if total_list7.isnull().values.any():
    # 对total_list7中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    total_list7 = total_list7.fillna(axis=1,method='ffill')
# print(total_list7)
total_list7 = np.array(total_list7).tolist() # 将DataFrame类型转为列表类型

j = 0
zong_list7 = [] # 总能源消耗
while True:
    sum = 0
    for i in total_list7:
        sum += i[j]
    zong_list7.append(sum)
    j = j + 1
    if j>=3:
        break
# print(zong_list7)

renewable_list7 = data.loc[(data['Country/Region']=='Western Asia') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Energy_Type']=='Total Renewable'),['F2010','F2015','F2020']]
if renewable_list7.isnull().values.any():
    # 对total_list7中的空缺进行填充处理，沿x轴方向，进行填充，选择前面的值
    renewable_list7 = renewable_list7.fillna(axis=1,method='ffill')
# print(renewable_list7)
renewable_list7 = np.array(renewable_list7).tolist() # 将DataFrame类型转为列表类型

j = 0
renew_list7 = [] # 可再生能源
while True:
    sum = 0
    for i in renewable_list7:
        sum += i[j]
    renew_list7.append(sum)
    j = j + 1
    if j>=3:
        break
# print(renew_list7)

other_list7 = []
other_list7 = data.loc[(data['Country/Region']=='Western Asia') & (data['Unit']=='Gigawatt-hours (GWh)')& (data['Technology']=='Other non-renewable energy'),['F2010','F2015','F2020']]
other_list7 = np.array(other_list7).tolist() # 将DataFrame类型转为列表类型
other_list7 = list(itertools.chain.from_iterable(other_list7)) # 将其转化为一维列表
# print(other_list7)

# 清洁能源
clean_list7 = []
for i in range(0,len(zong_list7),1):
    sum = zong_list7[i] - list7[i] - other_list7[i]
    clean_list7.append(sum)
# print(clean_list7)

# Western Asia:[[X1,X2,X3],[X1,X2,X3],[X1,X2,X3]]
Asia1_list1 = [] # 2010
Asia1_list2 = [] # 2015
Asia1_list3 = [] # 2020

Asia1_list1.append(list7[0]/zong_list7[0])
Asia1_list1.append(renew_list7[0]/zong_list7[0])
Asia1_list1.append(clean_list7[0]/zong_list7[0])

Asia1_list2.append(list7[1]/zong_list7[1])
Asia1_list2.append(renew_list7[1]/zong_list7[1])
Asia1_list2.append(clean_list7[1]/zong_list7[1])

Asia1_list3.append(list7[2]/zong_list7[2])
Asia1_list3.append(renew_list7[2]/zong_list7[2])
Asia1_list3.append(clean_list7[2]/zong_list7[2])
# print(Asia1_list1)
# print(Asia1_list2)
# print(Asia1_list3)

# Australia = [Australia_list1,Australia_list2,Australia_list3]
# dict['Australia'] = Australia
Western_Europe = [Europe_list1,Europe_list2,Europe_list3]
dict['Western Europe'] = Western_Europe
Northern_America = [America_list1,America_list2,America_list3]
dict['Northern America'] = Northern_America
Eastern_Asia = [Asia_list1,Asia_list2,Asia_list3]
dict['Eastern Asia'] = Eastern_Asia
# Latin_America = [Latin_list1,Latin_list2,Latin_list3]
# dict['Latin America'] = Latin_America
Africa = [Africa_list1,Africa_list2,Africa_list3]
dict['Africa'] = Africa
Western_Asia = [Asia1_list1,Asia1_list2,Asia1_list3]
dict['Western Asia'] = Western_Asia
print(dict)
print(getD(dict))
