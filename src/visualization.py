import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(
    "data/water_consumption.csv",
    parse_dates=["Date"]
)

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

df["Per_Capita_Liters"] = (
    df["Water_Consumption_m3"]
    / df["Population"]
    * 1000
)


# -----------------------------
# Annual consumption
# -----------------------------

annual = (
    df.groupby("Year")
    ["Water_Consumption_m3"]
    .mean()
)

plt.figure(figsize=(10, 6))

plt.plot(
    annual.index,
    annual.values,
    marker="o"
)

plt.title("Average Daily Water Consumption by Year")
plt.xlabel("Year")
plt.ylabel("Water Consumption (m³/day)")
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "figures/annual_water_consumption.png",
    dpi=300
)

plt.show()


# -----------------------------
# Monthly consumption
# -----------------------------

monthly = (
    df.groupby("Month")
    ["Water_Consumption_m3"]
    .mean()
)

plt.figure(figsize=(10, 6))

plt.bar(
    monthly.index,
    monthly.values
)

plt.title("Average Monthly Water Consumption")
plt.xlabel("Month")
plt.ylabel("Water Consumption (m³/day)")

plt.tight_layout()

plt.savefig(
    "figures/monthly_water_consumption.png",
    dpi=300
)

plt.show()


# -----------------------------
# Seasonal consumption
# -----------------------------

seasonal = (
    df.groupby("Season")
    ["Water_Consumption_m3"]
    .mean()
)

plt.figure(figsize=(8, 6))

plt.bar(
    seasonal.index,
    seasonal.values
)

plt.title("Average Water Consumption by Season")
plt.xlabel("Season")
plt.ylabel("Water Consumption (m³/day)")

plt.tight_layout()

plt.savefig(
    "figures/seasonal_water_consumption.png",
    dpi=300
)

plt.show()


# -----------------------------
# Temperature vs consumption
# -----------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Temperature_C",
    y="Water_Consumption_m3"
)

plt.title("Temperature vs Water Consumption")
plt.xlabel("Temperature (°C)")
plt.ylabel("Water Consumption (m³/day)")

plt.tight_layout()

plt.savefig(
    "figures/temperature_consumption.png",
    dpi=300
)

plt.show()


# -----------------------------
# Per-capita consumption
# -----------------------------

per_capita = (
    df.groupby("Zone")
    ["Per_Capita_Liters"]
    .mean()
)

plt.figure(figsize=(8, 6))

plt.bar(
    per_capita.index,
    per_capita.values
)

plt.title("Average Per-Capita Water Consumption")
plt.xlabel("Zone")
plt.ylabel("Liters/person/day")

plt.tight_layout()

plt.savefig(
    "figures/per_capita_consumption.png",
    dpi=300
)

plt.show()

# -----------------------------
# Precipitation vs Water Consumption
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(
    "data/water_consumption.csv",
    parse_dates=["Date"]
)

# Create scatter plot
plt.figure(figsize=(10, 6))

plt.scatter(
    df["Precipitation_mm"],
    df["Water_Consumption_m3"],
    alpha=0.5
)

plt.title("Precipitation vs Water Consumption")
plt.xlabel("Precipitation (mm)")
plt.ylabel("Water Consumption (m³/day)")

plt.grid(alpha=0.3)

plt.tight_layout()

# Save figure
plt.savefig(
    "figures/precipitation_consumption.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# -----------------------------
# Water Consumption Anomalies
# -----------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(
    "data/water_consumption.csv",
    parse_dates=["Date"]
)

# Calculate Z-score for each zone
df["Z_Score"] = (
    df.groupby("Zone")["Water_Consumption_m3"]
    .transform(lambda x: (x - x.mean()) / x.std())
)

# Identify anomalies
df["Anomaly"] = df["Z_Score"].abs() > 3

# Create figure
plt.figure(figsize=(12, 6))

# Plot each zone separately
for zone in df["Zone"].unique():

    zone_data = df[df["Zone"] == zone]

    plt.plot(
        zone_data["Date"],
        zone_data["Z_Score"],
        label=zone,
        alpha=0.7
    )

# Highlight anomalies
anomalies = df[df["Anomaly"]]

plt.scatter(
    anomalies["Date"],
    anomalies["Z_Score"],
    s=40,
    label="Anomalies"
)

# Anomaly thresholds
plt.axhline(
    3,
    linestyle="--",
    linewidth=1
)

plt.axhline(
    -3,
    linestyle="--",
    linewidth=1
)

# Labels
plt.title("Water Consumption Anomaly Detection")
plt.xlabel("Date")
plt.ylabel("Z-Score")

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

# Save figure
plt.savefig(
    "figures/consumption_anomalies.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()