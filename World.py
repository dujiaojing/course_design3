import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr
#数列归一化
def normalize(num):
    max= num[0]
    for n in num:
        if n>max:
            max = n
    min = num[0]
    for n in num:
        if n<min:
            min = n
    new = []
    for n in num:
        new.append((n-min)/(max-min))
    return new

#查看发电量数据表
energycsv = pd.read_csv('Energy_Transition.csv')
print("重复值数量",end=":")
print(energycsv.duplicated().sum())
#数据概览
print("基本数据")
energycsv.info()
print("取值情况：")
print(energycsv.nunique())

#查看温室气体数据
ghgcsv = pd.read_csv('Greenhouse_Gas.csv')
print("重复值数量",end=":")
print(energycsv.duplicated().sum())
print("基本数据")
ghgcsv.info()
print("取值情况：")
print(ghgcsv.nunique())
#删除无意义的数据
energycsv = energycsv.drop(columns=['ISO2','ISO3','Source','CTS_Name','CTS_Code','CTS_Full_Descriptor'])
energycsv = energycsv.drop(columns=['F2000','F2001','F2002','F2003','F2004','F2005','F2006','F2007','F2008','F2009'])
ghgcsv = ghgcsv.drop(columns=['ISO2','ISO3','Indicator','Unit','Source','CTS_Name','CTS_Code','CTS_Full_Descriptor','Scale'])
#查看特殊列的取值
energycolumns = energycsv.columns[2:6]
for i in energycolumns:
    print(i,end=":")
    print(energycsv[i].unique())
ghgcolumns = ghgcsv.columns[1:4]
for i in ghgcolumns:
    print(i,end=":")
    print(ghgcsv[i].unique())
#########################################################################################
#获取Country/Region为World的数据
worldenergycsv = energycsv.loc[energycsv['Country/Region']=='World']
worldghgcsv = ghgcsv.loc[ghgcsv['Country/Region']=='World']
#只要发电量数据
worldenergycsv = worldenergycsv.loc[energycsv['Unit']=='Gigawatt-hours (GWh)']
print("查看缺失值：")
print(worldghgcsv.isnull().sum())
print("查看缺失值：")
print(worldenergycsv.isnull().sum())
#不同类型能源类型用量变化折线图，一个能源一条线（每年）百分比
technology = worldenergycsv['Technology'].tolist()
fyears = worldenergycsv.columns.tolist()[-11:]
gwhratio = [[] for j in range(len(technology))]
for year in fyears:
    gwhsum = worldenergycsv[year].sum()
    templists = worldenergycsv[year].tolist()
    for j in range(0,len(templists)):
        gwhratio[j].append(templists[j]/gwhsum)
years = []
for i in range(0,len(fyears)):
    years.append(fyears[i])
    years[i] = years[i][1:]
    years[i] = int(years[i])
for j in range(0,len(gwhratio)):
    plt.plot(years,gwhratio[j],label = technology[j])
plt.legend()
plt.show()
#可再生能源与不可再生能源占比（每年）柱形图
renewable = []
templists = worldenergycsv['Energy_Type'].tolist()
for j in range(0,len(technology)):
    if templists[j] == 'Total Renewable':
        renewable.append(j)
gwhrenew = []
gwhnonrenew = []
for j in range(0,len(gwhratio[0])):
    sum = 0
    for i in range(0,len(gwhratio)):
        if i in renewable:
            sum = sum + gwhratio[i][j]
    gwhrenew.append(sum)
    gwhnonrenew.append(1-sum)
years1 = [i-0.15 for i in years]
years2 = [i+0.15 for i in years]
plt.bar(years1,gwhrenew,width = 0.3,label = 'Renewable')
plt.bar(years2,gwhnonrenew,width=0.3,label = 'Non-Renewable')
plt.legend()
plt.show()

#柱状图，横坐标为年份，每一个坐标五条数据，分别是不同温室气体的含量
N = worldghgcsv.loc[worldghgcsv['Gas_Type']=='Nitrous oxide']
C = worldghgcsv.loc[worldghgcsv['Gas_Type']=='Carbon dioxide']
F = worldghgcsv.loc[worldghgcsv['Gas_Type']=='Fluorinated gases']
M = worldghgcsv.loc[worldghgcsv['Gas_Type']=='Methane']
G = worldghgcsv.loc[worldghgcsv['Gas_Type']=='Greenhouse gas']
Nlist = []
Clist = []
Flist = []
Mlist = []
Glist = []
for year in fyears:
    Nlist.append(N[year].sum())
    Clist.append(C[year].sum())
    Flist.append(F[year].sum())
    Mlist.append(M[year].sum())
    Glist.append(G[year].sum())
years1 = [i-0.3 for i in years]
years2 = [i-0.1 for i in years]
years3 = [i+0.1 for i in years]
years4 = [i+0.3 for i in years]
plt.bar(years1,Nlist,width=0.2,label = 'Nitrous oxide')
plt.bar(years2,Clist,width=0.2,label = 'Carbon dioxide')
plt.bar(years3,Nlist,width=0.2,label = 'Fluorinated gases')
plt.bar(years4,Clist,width=0.2,label = 'Methane')
plt.show()
plt.bar(years,Glist,width=0.5,label='Greenhouse gas')
plt.legend()
plt.show()
Vlist = [0,]
for i in range(1,len(Glist)):
    Vlist.append(Glist[i]-Glist[i-1])
plt.bar(years,Vlist,width=0.5)
plt.show()
#柱状图与折线图，折线为不同能源随年份变化发电量变化图，
Vlist = normalize(Vlist)
plt.bar(years,Vlist,width=0.5)
for j in range(0,len(gwhratio)):
    plt.plot(years,gwhratio[j],label = technology[j])
plt.legend()
plt.show()

#计算皮尔森系数
#可再生能源
r = pearsonr(gwhrenew,Glist)
print("可再生能源使用比例与温室气体排放量的相关性系数：",end="")
print(r[0])
#化石能源
r = pearsonr(gwhratio[1],Glist)
print("化石能源使用比例与温室气体排放量的相关性系数：",end="")
print(r[0])
#清洁能源
gwhclear = []
for i in range(0,11):#按照年份循环
    gwhclear.append(1-gwhratio[1][i]-gwhratio[6][i])#除了能源1和能源6在i年所占的比例，其余都算入
r = pearsonr(gwhclear,Glist)
print("清洁能源使用比例与温室气体排放量的相关性系数：",end="")
print(r[0])











