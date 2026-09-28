import numpy as np
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)


# For reproducible results
np.random.seed(42)

# Create dates for two years
dates = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
    freq="D"
)

zones = {
    "Zone_1": 45000,
    "Zone_2": 60000,
    "Zone_3": 35000,
    "Zone_4": 50000,
}

data = []

for date in dates:

    month = date.month

    # Seasonal temperature
    if month in [12, 1, 2]:
        temperature = np.random.normal(2, 3)
    elif month in [3, 4, 5]:
        temperature = np.random.normal(15, 4)
    elif month in [6, 7, 8]:
        temperature = np.random.normal(28, 4)
    else:
        temperature = np.random.normal(14, 4)

    # Simulated precipitation
    if month in [11, 12, 1, 2, 3]:
        precipitation = np.random.gamma(2, 5)
    else:
        precipitation = np.random.gamma(1, 2)

    for zone, population in zones.items():

        # Base consumption
        base_consumption = population * 0.12

        # Higher consumption in hot weather
        temperature_effect = max(temperature - 20, 0) * population * 0.002

        # Small reduction after rainfall
        rainfall_effect = precipitation * population * 0.0005

        # Random daily variation
        random_effect = np.random.normal(0, population * 0.01)

        consumption = (
            base_consumption
            + temperature_effect
            - rainfall_effect
            + random_effect
        )

        consumption = max(consumption, 0)

        data.append(
            {
                "Date": date,
                "Zone": zone,
                "Population": population,
                "Temperature_C": round(temperature, 2),
                "Precipitation_mm": round(precipitation, 2),
                "Day_of_Week": date.day_name(),
                "Water_Consumption_m3": round(consumption, 2),
            }
        )


df = pd.DataFrame(data)

# Save dataset
df.to_csv(
    DATA_DIR / "water_consumption.csv",
    index=False
)



print("Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(df.head())