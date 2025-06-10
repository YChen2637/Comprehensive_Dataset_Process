## **Data Processing and Visualization**
### 1 Introduction

This project aims to visually present cotton-related and weather data through data visualization. The folder contains the following three key documents:

|**Author**|©AuroraLab |
|:--------:   |:-------------------------------------|
|**ChartCottonDefault**      | Generates charts for cotton sensor default data |
|**ChartCottonYield**  | Generates charts for cotton yield data |
|**ChartWeather**  | Generates charts for weather data (1981-2023)         |

These charts help analyze cotton growth conditions and yield trends, providing data support for relevant research.

### **Use Note for Visualization Scripts of Cotton Field Data**

This repository contains three Python scripts for visualizing multi-source data collected from a cotton field experiment. These scripts are: `Chart_CottonDefault.py`, `chart-yield.py`, and `Chart_Weather.py`. Each serves a distinct analytical purpose and requires specific datasets to be available in a predefined directory structure. Below are usage guidelines and path configuration instructions to ensure successful execution.

#### **1. Directory Structure & Path Configuration**

All scripts rely on relative file paths. Users must ensure that the project directory is organized as follows:

```
ProjectRoot/
│
├── DataProcessingDemonstration/
	├── ChartCottonDefault.py
	├── ChartCottonYield.py
	├── ChartWeather.py
├── CottonSensor/
│   ├── ConductSensor.csv
│   ├── HeatFluxSensor.csv
│   ├── HumiditySensor.csv
│   ├── InsectSensor.csv
│   ├── PHSensor.csv
│   ├── SoilNutSensor.csv
│   ├── SporeSensor.csv
│   └── TemSensor.csv
│
├── Weather/
│   └── Weather.CSV
│
└── CottonYield.csv

```

**Important:** The relative paths such as `../CottonSensor/ConductSensor.csv` imply that the script is being executed **from within a subfolder** (e.g., `scripts/`) or **within an IDE like PyCharm** where the working directory is set at a higher level. Adjust these paths based on your working directory or move the script files to the project root.

------

#### **2. Script Functions and Data Requirements**

**`ChartCottonDefault.py`**

- **Purpose:** Visualizes daily data completeness across eight soil/environmental sensors (e.g., conductivity, temperature, pH) from July 1 to September 11, 2024.
- **Inputs:** Eight `.csv` sensor files from the `CottonSensor` directory.
- **Output:** A horizontal bar plot showing data availability, saved as `flg_4_Cotton_0701~0911_default.pdf`.

**`ChartYield.py`**

- **Purpose:** Compares cotton yields across different water treatment conditions.
- **Input:** `CottonYield.csv` containing treatment information and yield data.
- **Output:** Horizontal bar chart visualizing yield variation, saved as `flg_7_Cotton_yield.pdf`.

**`ChartWeather.py`**

- **Purpose:** Calculates and plots annual trends in solar radiation, maximum/minimum temperature, and rainfall from 1981 to 2023.
- **Input:** A historical weather file `Weather.CSV` with specific columns such as `DATE`, `RAIN(mm/day)`, `TMAX(℃)`, `TMIN(℃)`, and `SRAD(MJ/(m2*day))`.
- **Output:** Four time-series plots:
  - `fig_8_annual_solar_radiation.pdf`
  - `fig_8_annual_maximum_temperature.pdf`
  - `fig_8_annual_minimum_temperature.pdf`
  - `fig_8_annual_Rainfall.pdf`

------

#### **3. Dependencies**

Ensure the following Python libraries are installed in your environment:

```
pip install numpy pandas matplotlib
```

------

#### **4. Encoding and Format Notes**

- CSV files should be encoded in UTF-8 or ISO-8859-1 as specified in the scripts.
- Ensure date formats match `'YYYY-MM-DD HH:MM:SS'` when parsing with `pd.to_datetime`.

------

#### **5. Reproducibility Tip**

To ensure full compatibility and prevent relative path errors, consider running the scripts from the project root directory using:

```
python ChartCottonDefault.py
python ChartYield.py
python ChartWeather.py
```

Or configure the working directory in your IDE (e.g., PyCharm) to point to the project root.

### Copyright
Copyright © 2024 AuroraLab of Tsinghua University and Xinjiang University. All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of AuroraLab of Tsinghua University and Xinjiang University.
Email: heliang@mail.tsinghua.edu.cn.

