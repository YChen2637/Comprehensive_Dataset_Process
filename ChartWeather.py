# @Descripttion ：
# -*- codeing: utf-8 -*-
# @time ：2025/5/7 16:44
# @Author : Ruifeng Xu
# @Site : 
# @file : Chart_Weather.py
# @Sofeware : PyCharm




import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt


file_path="../Weather/Weather_1981-2024.CSV"

Rain_year=[]
max_temp_year=[]
min_temp_year=[]
SRAD_year=[]
years=[]
years1=[]
Weather = pd.read_csv(file_path, encoding='ISO-8859-1')
print(Weather.columns)
# Dates=pd.DataFrame(Weather.iloc[:,0]).dropna()
# RAIN=pd.DataFrame(Weather.iloc[:,1]).dropna()
# TMAX=pd.DataFrame(Weather.iloc[:,4]).dropna()
# TMIN=pd.DataFrame(Weather.iloc[:,5]).dropna()
# SRAD=pd.DataFrame(Weather.iloc[:,6]).dropna()
# print(Dates)
for i in range(1981,2024):
    Rain = []
    max_temp = []
    min_temp = []
    SRAD = []
    years.append(i)
    if i!=2021:
        years1.append(i)
    for index, row in Weather.iterrows():
        date = row['DATE']
        year = date.split('/')[0]  # 提取年份
        if year == str(i):
            Rain.append(row['RAIN(mm/day)'])
            max_temp.append(row['TMAX(¡ã)'])
            min_temp.append(row['TMIN(¡ã)'])
            if year!='2021':
                SRAD.append(row['SRAD(MJ/(m2*day))'])
        else:
            continue
    if i ==2021:
        max_temp_sum = sum(max_temp)
        min_temp_sum = sum(min_temp)
        max_temp_len = len(max_temp)
        min_temp_len = len(min_temp)
        Rain_sum = sum(Rain)
        Rain_len = len(Rain)
        max_temp_avg = max_temp_sum / max_temp_len
        max_temp_avg = round(max_temp_avg, 2)
        min_temp_avg = min_temp_sum / min_temp_len
        min_temp_avg = round(min_temp_avg, 2)
        Rain_avg = Rain_sum / Rain_len
        Rain_avg = round(Rain_avg, 2)
        max_temp_year.append(max_temp_avg)
        min_temp_year.append(min_temp_avg)
        Rain_year.append(Rain_avg)
    else:
        SRAD_sum = sum(SRAD)
        SRAD_len = len(SRAD)
        SRAD_avg = SRAD_sum / SRAD_len
        SRAD_avg = round(SRAD_avg, 2)
        SRAD_year.append(SRAD_avg)
        max_temp_sum = sum(max_temp)
        min_temp_sum = sum(min_temp)
        max_temp_len = len(max_temp)
        min_temp_len = len(min_temp)
        Rain_sum = sum(Rain)
        Rain_len = len(Rain)
        max_temp_avg = max_temp_sum / max_temp_len
        max_temp_avg = round(max_temp_avg, 2)
        min_temp_avg = min_temp_sum / min_temp_len
        min_temp_avg = round(min_temp_avg, 2)
        Rain_avg = Rain_sum / Rain_len
        Rain_avg = round(Rain_avg, 2)
        max_temp_year.append(max_temp_avg)
        min_temp_year.append(min_temp_avg)
        Rain_year.append(Rain_avg)




# -------------------------------------annual_solar_radiation--------------------------------------------
fig, ax = plt.subplots()

plt.plot(years1, SRAD_year, color='darkgreen', linestyle=':', linewidth=2, markersize=8)  # 自定义颜色和线宽

plt.title('Average annual solar radiation', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12)
plt.ylabel('SRAD(MJ/m² day)', fontsize=12)
plt.xticks(years1[::6],)
plt.savefig('fig_8_annual_solar_radiation.pdf', format='pdf')
plt.show()

# # -------------------------------------annual_maximum_temperature--------------------------------------------
fig, ax = plt.subplots()
plt.plot(years, max_temp_year ,color='red', linestyle='-.', linewidth=2, )  # 自定义颜色和线宽
ax.fill_between(years, max_temp_year, color='red', alpha=0.3)
plt.title('Average annual maximum temperature', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12)
plt.ylabel('TMAX(℃)', fontsize=12)
plt.xticks(years[::6],)
plt.savefig('fig_8_annual_maximum_temperature.pdf', format='pdf')
plt.show()
#
# # -------------------------------------annual_maximum_temperature--------------------------------------------
fig, ax = plt.subplots()
plt.plot(years, min_temp_year ,color='red', linestyle='-.', linewidth=2, )  # 自定义颜色和线宽
ax.fill_between(years, min_temp_year, color='red', alpha=0.3)
plt.title('Average annual minimum temperature', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12)
plt.ylabel('Tmin(℃)', fontsize=12)
plt.xticks(years[::6],)
plt.savefig('fig_8_annual_minimum_temperature.pdf', format='pdf')
plt.show()
#
# # -------------------------------------annual_Rainfall--------------------------------------------
fig, ax = plt.subplots()
plt.plot(years, Rain_year ,color='dodgerblue',linestyle='-.', linewidth=2, )  # 自定义颜色和线宽
# ax.fill_between(years, Rain_year, color='blue',alpha=0.3 )
plt.title('Average annual Rainfall', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12)
plt.ylabel('Rain(mm)', fontsize=12)
plt.xticks(years[::6],)
plt.savefig('fig_8_annual_Rainfall.pdf', format='pdf')
plt.show()



