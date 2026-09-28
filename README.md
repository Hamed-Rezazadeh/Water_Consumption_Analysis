#  Water Consumption Analysis with Python

> An end-to-end Python project for analyzing water consumption patterns, per-capita water use, seasonal variability, weather relationships, and consumption anomalies.

---

##  Project Overview

This project analyzes daily water consumption data across four zones using Python and statistical data-analysis techniques.

The analysis focuses on understanding:

- Water consumption patterns
- Differences between zones
- Per-capita water consumption
- Seasonal variability
- Annual changes
- Relationships between water consumption and temperature
- Relationships between water consumption and precipitation
- Detection of unusual consumption patterns

The project demonstrates how Python can be used to transform raw water-consumption data into practical analytical and hydrological insights.

---

##  Project Objectives

The main objectives of this project are to:

- Analyze daily water consumption patterns
- Compare water consumption between different zones
- Calculate per-capita water consumption
- Examine seasonal and monthly consumption patterns
- Investigate the relationship between temperature and water consumption
- Investigate the relationship between precipitation and water consumption
- Compare annual consumption patterns
- Detect consumption anomalies using Z-scores
- Demonstrate practical Python-based water-resources data analysis

---

##  Dataset

The dataset contains daily water-consumption observations for four zones during 2024 and 2025.

### Main Variables

| Variable | Description |
|---|---|
| `Date` | Observation date |
| `Zone` | Water-consumption zone |
| `Population` | Population of the zone |
| `Temperature_C` | Daily temperature in °C |
| `Precipitation_mm` | Daily precipitation in mm |
| `Day_of_Week` | Day of the week |
| `Water_Consumption_m3` | Daily water consumption in cubic meters |

### Derived Variables

Additional variables were created during the analysis:

| Variable | Description |
|---|---|
| `Year` | Calendar year |
| `Month` | Month number |
| `Month_Name` | Month name |
| `Season` | Season |
| `Per_Capita_Consumption` | Per-capita daily consumption |
| `Per_Capita_Liters` | Per-capita consumption in liters |
| `Z_Score` | Consumption anomaly score |
| `Zone_Z_Score` | Zone-specific anomaly score |

---

#  Analytical Workflow

```text
Raw Water Consumption Data
          │
          ▼
Data Cleaning & Preparation
          │
          ▼
Exploratory Data Analysis
          │
          ├── Annual Analysis
          ├── Monthly Analysis
          ├── Seasonal Analysis
          └── Zone Comparison
          │
          ▼
Per-Capita Consumption Analysis
          │
          ▼
Weather Relationship Analysis
          │
          ├── Temperature
          └── Precipitation
          │
          ▼
Anomaly Detection
          │
          ▼
Hydrological Interpretation


1. Data Preparation

The first stage of the project includes:

Loading the dataset
Checking data types
Checking missing values
Converting dates
Creating temporal variables
Creating seasonal classifications
Calculating per-capita consumption
Calculating standardized consumption scores

The purpose of this stage is to create a clean dataset suitable for statistical analysis and visualization.

2. Annual Water Consumption Analysis

Annual average daily water consumption was calculated for 2024 and 2025.

| Year | Average Daily Consumption (m³/day) |
| ---- | ---------------------------------: |
| 2024 |                           5,806.37 |
| 2025 |                           5,755.74 |

The results show a modest decrease in average daily consumption between 2024 and 2025.

This comparison describes the observed values in the dataset and should not be interpreted as evidence of a long-term consumption trend because the analysis covers only two years.

3. Zone-Based Consumption Analysis

Water consumption was compared across four zones.

The analysis considers both:

Total water consumption
Average daily consumption

Zone-level comparison helps identify differences in demand that may be associated with population size, environmental conditions, or consumption behavior.

Key Result

Zone_2 had the highest total water consumption among the four zones.

Because total consumption is influenced by population size, total consumption should be interpreted together with per-capita consumption.

4. Per-Capita Water Consumption

Per-capita consumption was calculated to provide a more meaningful comparison between zones with different population sizes.

The highest average per-capita consumption was observed in:

Zone_3 → 122.61 liters/person/day

The estimated average per-capita values were:
| Zone   | Per-Capita Consumption |
| ------ | ---------------------: |
| Zone_3 |    122.61 L/person/day |
| Zone_2 |    121.80 L/person/day |
| Zone_4 |    121.77 L/person/day |
| Zone_1 |    120.80 L/person/day |

This analysis demonstrates why population-normalized indicators can provide additional insight beyond total water consumption.

5. Seasonal Water Consumption

Seasonal average water consumption was analyzed across the four seasons.

The average daily consumption values were:
| Season | Average Daily Consumption (m³/day) |
| ------ | ---------------------------------: |
| Summer |                           6,459.75 |
| Spring |                           5,591.57 |
| Autumn |                           5,584.53 |
| Winter |                           5,481.47 |

Summer had the highest average daily water consumption in the dataset.

The difference between summer and winter consumption may be associated with seasonal conditions, including higher temperatures and changes in water-use behavior.

6. Temperature and Water Consumption

The relationship between temperature and water consumption was investigated using correlation analysis.

The overall Pearson correlation coefficient was:

r = 0.288

This indicates a positive association between temperature and water consumption in the analyzed dataset.

However, correlation does not imply causation.

Other variables such as population, season, precipitation, day of the week, and behavioral patterns may also influence water demand.

Summer Temperature Relationship

For the summer period, the correlation coefficient was approximately:

r = 0.259

This suggests that temperature remains positively associated with water consumption during summer, although the relationship is not strong.

7. Precipitation and Water Consumption

Precipitation was also included as an explanatory environmental variable.

The purpose was to investigate whether rainfall conditions are associated with changes in daily water consumption.

The relationship should be interpreted cautiously because precipitation is only one of several factors affecting water demand.

8. Water Consumption Anomaly Detection

Consumption anomalies were identified using Z-scores.

The analysis detected:

150 zone-based anomalous observations

The distribution of detected anomalies was:
| Zone   | Number of Anomalies |
| ------ | ------------------: |
| Zone_1 |                  39 |
| Zone_2 |                  38 |
| Zone_3 |                  35 |
| Zone_4 |                  38 |

The Z-score approach provides a simple statistical method for identifying observations that differ substantially from the typical consumption pattern.

An anomaly does not necessarily indicate an error.

Possible explanations may include:

Unusual demand
Weather conditions
Operational changes
Special events
Measurement issues
Changes in consumption behavior

9. Key Findings
The main findings of the analysis are:
Water consumption varies considerably between zones.
Zone_2 had the highest total water consumption.
Zone_3 had the highest average per-capita consumption at approximately 122.61 L/person/day.
Summer had the highest average daily consumption at approximately 6,459.75 m³/day.
Winter had the lowest seasonal average at approximately 5,481.47 m³/day.
Average daily consumption decreased from 5,806.37 m³/day in 2024 to 5,755.74 m³/day in 2025.
Temperature showed a positive correlation with water consumption, with an overall Pearson correlation of approximately 0.288.
The analysis identified 150 zone-based anomalous observations using Z-score analysis.
Per-capita indicators provide additional information that cannot be obtained from total consumption alone.
Environmental and temporal variables should be considered together when analyzing water demand.


Limitations:

Several limitations should be considered when interpreting the results.

Short Study Period

The dataset covers only 2024 and 2025. Therefore, the results cannot be used to establish long-term water-demand trends.

Synthetic Dataset

The dataset is synthetic and is intended for analytical practice and portfolio demonstration.

Correlation vs. Causation

Observed correlations between temperature and water consumption do not establish causal relationships.

Population Effects

Total water consumption is strongly influenced by population size. Therefore, comparisons between zones should consider per-capita indicators.

Anomaly Detection

Z-score-based anomaly detection identifies statistically unusual observations but does not automatically determine the physical or operational cause of an anomaly.


Skills Demonstrated:

This project demonstrates practical experience in:

Python programming
Data cleaning
Data preprocessing
Exploratory Data Analysis (EDA)
Pandas
NumPy
Statistical analysis
Time-series analysis
Water-demand analysis
Per-capita analysis
Correlation analysis
Anomaly detection
Data visualization
Hydrological data interpretation


Project Structure:
Water_Consumption_Analysis/
│
├── data/
│   └── water_consumption.csv
│
├── figures/
│   ├── annual_water_consumption.png
│   ├── monthly_water_consumption.png
│   ├── seasonal_water_consumption.png
│   ├── temperature_consumption.png
│   ├── precipitation_consumption.png
│   ├── per_capita_consumption.png
│   └── consumption_anomalies.png
│
├── notebooks/
│   └── Water_Consumption_Analysis.ipynb
│
├── src/
│   └── water_consumption_analysis.py
│
├── README.md
├── requirements.txt
└── .gitignore

How to Run
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
2. Navigate to the project directory
cd Water_Consumption_Analysis
3. Install dependencies
pip install -r requirements.txt
4. Open Jupyter Notebook
jupyter notebook
Open:
notebooks/Water_Consumption_Analysis.ipynb
Run the notebook cells sequentially.


Reproducibility

The project separates:

Input data
Analysis notebook
Python source code
Generated visualizations
Project documentation

The analysis can be reproduced by installing the listed dependencies and running the Jupyter Notebook.


Conclusion

This project demonstrates how Python can be used to analyze water-consumption data and extract meaningful information for water-resources and demand-management applications.

The analysis combines temporal analysis, zone-level comparison, per-capita indicators, environmental variables, correlation analysis, and anomaly detection.

Although the dataset is synthetic and covers only two years, the workflow can be adapted to real-world water-demand datasets from municipalities, utilities, water companies, and other water-resources organizations.

The project demonstrates the application of Python-based data analysis to practical water-resources problems.


Project Status

Portfolio Project — Completed Analytical Workflow

The project is designed to demonstrate practical Python, statistical, and water-resources data-analysis skills.


Keywords

Python Pandas NumPy Matplotlib Seaborn Water Resources
Water Consumption Water Demand Hydrology Time Series Analysis
Data Analysis EDA Per Capita Consumption Correlation Analysis
Anomaly Detection Water Management