import pandas as pd
import numpy as np
from scipy import stats


# -----------------------------
# Load data
# -----------------------------

df = pd.read_csv(
    "data/water_consumption.csv",
    parse_dates=["Date"]
)


# -----------------------------
# Time features
# -----------------------------

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.month_name()

season_map = {
    12: "Winter",
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Autumn",
    10: "Autumn",
    11: "Autumn"
}

df["Season"] = df["Month"].map(season_map)


# -----------------------------
# Per-capita consumption
# -----------------------------

df["Per_Capita_Consumption"] = (
    df["Water_Consumption_m3"]
    / df["Population"]
)

df["Per_Capita_Liters"] = (
    df["Per_Capita_Consumption"] * 1000
)


# -----------------------------
# Overall Z-score
# -----------------------------

df["Z_Score"] = stats.zscore(
    df["Water_Consumption_m3"]
)

df["Anomaly"] = (
    df["Z_Score"].abs() > 3
)


# -----------------------------
# Zone-based Z-score
# -----------------------------

df["Zone_Z_Score"] = (
    df.groupby("Zone")["Water_Consumption_m3"]
    .transform(
        lambda x: (x - x.mean()) / x.std()
    )
)

df["Zone_Anomaly"] = (
    df["Zone_Z_Score"].abs() > 3
)


# -----------------------------
# Annual analysis
# -----------------------------

annual_consumption = (
    df.groupby("Year")
    ["Water_Consumption_m3"]
    .mean()
)


# -----------------------------
# Seasonal analysis
# -----------------------------

seasonal_consumption = (
    df.groupby("Season")
    ["Water_Consumption_m3"]
    .mean()
)


# -----------------------------
# Zone analysis
# -----------------------------

zone_consumption = (
    df.groupby("Zone")
    ["Water_Consumption_m3"]
    .mean()
)


# -----------------------------
# Per-capita analysis
# -----------------------------

per_capita_by_zone = (
    df.groupby("Zone")
    ["Per_Capita_Liters"]
    .mean()
)


# -----------------------------
# Temperature correlation
# -----------------------------

temperature_correlation = (
    df["Temperature_C"]
    .corr(df["Water_Consumption_m3"])
)


# -----------------------------
# Precipitation correlation
# -----------------------------

precipitation_correlation = (
    df["Precipitation_mm"]
    .corr(df["Water_Consumption_m3"])
)


# -----------------------------
# Anomaly summary
# -----------------------------

anomaly_summary = (
    df[df["Zone_Anomaly"]]
    .groupby("Zone")
    .size()
)


# -----------------------------
# Print results
# -----------------------------

print("\nAnnual Consumption:")
print(annual_consumption)

print("\nSeasonal Consumption:")
print(seasonal_consumption)

print("\nZone Consumption:")
print(zone_consumption)

print("\nPer-Capita Consumption:")
print(per_capita_by_zone)

print("\nTemperature Correlation:")
print(temperature_correlation)

print("\nPrecipitation Correlation:")
print(precipitation_correlation)

print("\nZone Anomalies:")
print(anomaly_summary)