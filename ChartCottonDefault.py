# @Descripttion ：
# -*- codeing: utf-8 -*-
# @time ：2025/5/7 16:23
# @Author : Ruifeng Xu
# @Site : 
# @file : Chart_CottonDefault.py
# @Sofeware : PyCharm



import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt

file_path_conduct="../CottonSensor/ConductSensor.csv"
file_path_heat="../CottonSensor/HeatFluxSensor.csv"
file_path_humidity="../CottonSensor/HumiditySensor.csv"
file_path_insect="../CottonSensor/InsectSensor.csv"
file_path_ph="../CottonSensor/PHSensor.csv"
file_path_nut="../CottonSensor/SoilNutSensor.csv"
file_path_spore="../CottonSensor/SporeSensor.csv"
file_path_tem="../CottonSensor/TemSensor.csv"
ConductSensor = pd.read_csv(file_path_conduct)
HeatFluxSensor = pd.read_csv(file_path_heat)
HumiditySensor = pd.read_csv(file_path_humidity)
InsectSensor = pd.read_csv(file_path_insect)
PHSensor = pd.read_csv(file_path_ph)
SoilNutSensor = pd.read_csv(file_path_nut)
SporeSensor = pd.read_csv(file_path_spore)
TemSensor = pd.read_csv(file_path_tem)

print(TemSensor)
date_range = pd.date_range(start='2024-07-01', end='2024-09-11', freq='D').date
sensors =['Conduct','HeatFlux',
          'Humidity','Insect','PH','SoilNut','Spore','Tem']
continuous_data = pd.DataFrame(index=date_range,columns=[sensor for sensor in sensors])

Cotton_ConductSensor_default = ConductSensor.loc[:, ["collect_time"]]
Cotton_HeatFluxSensor_default = HeatFluxSensor.loc[:, ["collect_time"]]
Cotton_HumiditySensor_default = HumiditySensor.loc[:, ["collect_time"]]
Cotton_InsectSensor_default = InsectSensor.loc[:, ["collect_time"]]


Cotton_PHSensor_default = PHSensor.loc[:, ["collect_time"]]
Cotton_SoilNutSensor_default = SoilNutSensor.loc[:, ["collect_time"]]
Cotton_SporeSensor_default = SporeSensor.loc[:, ["collect_time"]]
Cotton_TemSensor_default = TemSensor.loc[:, ["collect_time"]]
Cotton_ConductSensor_default['collect_time'] = pd.to_datetime(Cotton_ConductSensor_default['collect_time'], format='%Y-%m-%d %H:%M:%S').dt.date
Cotton_HeatFluxSensor_default['collect_time'] = pd.to_datetime(Cotton_HeatFluxSensor_default['collect_time'], format='%Y-%m-%d %H:%M:%S').dt.date
Cotton_HumiditySensor_default['collect_time'] = pd.to_datetime(Cotton_HumiditySensor_default['collect_time'], format='%Y-%m-%d %H:%M:%S').dt.date
Cotton_InsectSensor_default['collect_time'] = pd.to_datetime(Cotton_InsectSensor_default['collect_time'], format='%Y-%m-%d %H:%M:%S').dt.date
Cotton_PHSensor_default['collect_time'] = pd.to_datetime(Cotton_PHSensor_default['collect_time'], format='%Y-%m-%d %H:%M:%S').dt.date
Cotton_SoilNutSensor_default['collect_time'] = pd.to_datetime(Cotton_SoilNutSensor_default['collect_time'], format='%Y-%m-%d %H:%M:%S').dt.date
Cotton_SporeSensor_default['collect_time'] = pd.to_datetime(Cotton_SporeSensor_default['collect_time'], format='%Y-%m-%d %H:%M:%S').dt.date
Cotton_TemSensor_default['collect_time'] = pd.to_datetime(Cotton_TemSensor_default['collect_time'], format='%Y-%m-%d %H:%M:%S').dt.date


sensors_default=[Cotton_ConductSensor_default,Cotton_HeatFluxSensor_default,
                 Cotton_HumiditySensor_default,Cotton_InsectSensor_default,
                 Cotton_PHSensor_default,Cotton_SoilNutSensor_default,Cotton_SporeSensor_default,Cotton_TemSensor_default]

for sensor ,sensor_default in zip(continuous_data.columns,sensors_default):
    for date in continuous_data.index:

        matched_rows = sensor_default[sensor_default['collect_time'] == date]
        if not matched_rows.empty:
            continuous_data.at[date, sensor] = matched_rows['collect_time'].iloc[0]


width_ratios = [1] * len(sensors)
sensors = continuous_data.columns
dates = continuous_data.index
fig, axes = plt.subplots(nrows=1, ncols=len(sensors), figsize=(12, 6), sharey=True,width_ratios=width_ratios)

colors =[cm.Greens(np.random.normal(loc=0.9, scale=0.3, size=1)[0]) for _ in sensors]
if len(sensors) == 1:
    axes = [axes]

datetime_index = pd.DatetimeIndex(continuous_data.index)
formatted_dates = datetime_index.strftime('%Y-%m-%d')

for i,(ax, sensor,color1) in enumerate(zip(axes, sensors,colors)):
    data_presence = np.where(continuous_data[sensor].notnull(), 1, 0)
    percentage_present = int(np.mean(data_presence)*100)
    ax.barh(dates,data_presence,label=sensor, height=1, align='center', color=color1)
    ax.set_xlabel(f'{sensor}:{percentage_present}% ',fontsize=12)
    ax.set_yticks([])
    ax.set_xticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)




num_ticks = 10
tick_interval = len(dates) // (num_ticks - 1) if len(dates) > num_ticks else 1
ticks = np.arange(0, len(dates), tick_interval)
plt.yticks(dates[ticks], fontsize=10)
fig.suptitle("Cotton_default", fontsize=16)
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.tight_layout()
plt.savefig('flg_4_Cotton_0701~0911_default.pdf', bbox_inches='tight',format='pdf')
plt.show()