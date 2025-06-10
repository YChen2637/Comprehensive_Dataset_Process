# @Descripttion ：
# -*- codeing: utf-8 -*-
# @time ：2024/12/14 23:52
# @Author : Ruifeng Xu
# @Site :
# @file : chart-yield.py
# @Sofeware : PyCharm

import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt, cm
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize




file_path="../CottonYield.csv"
Cotton_Yield = pd.read_csv(file_path, encoding='utf-8')

Cotton_production=pd.DataFrame(Cotton_Yield.iloc[:,15]).dropna()
Cotton_treat=pd.DataFrame(Cotton_Yield.iloc[:,0].drop_duplicates())
Cotton_production.columns=['Yield']
Cotton_treat.columns=['Treatment']
Cotton_production = Cotton_production.reset_index(drop=True)
Cotton_treat = Cotton_treat.reset_index(drop=True)

Cotton_production=pd.concat([Cotton_treat,Cotton_production],axis=1)

Cotton_production=Cotton_production.sort_values(by='Yield', ascending=True)





plt.figure(figsize=(14, 8))
fig, ax = plt.subplots()


colors = [cm.Greens(i) for i in np.linspace(0.2, 1, len(Cotton_production))]


bars = ax.barh(Cotton_production['Treatment'], Cotton_production['Yield'], color=colors)
for bar in bars:
    width = bar.get_width()
    y_pos = bar.get_y() + bar.get_height() / 2
    ax.text(width, y_pos, f'{width:.1f}', va='center', ha='left', fontsize=8)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.title('Corn - Water Treatment - Yield')  # 标题
plt.xlabel('Yield (kg/mu)', fontsize=10)  # x轴标签
plt.ylabel('Categories', fontsize=10)  # y轴标签

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.savefig('flg_7_Cotton_yield.pdf', format='pdf')