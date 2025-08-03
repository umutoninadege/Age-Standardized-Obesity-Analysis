# main.py

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Optional: Show plots inline if you use Jupyter, but it's ignored in VS Code .py files
# %matplotlib inline

# Step 2: Load Dataset
df = pd.read_csv("RELAY_WHS.csv")

# Step 3: Show Basic Info
print("\n--- Dataset Info ---")
print(df.info())
print(df.head())

# Step 4: Clean and Rename Columns
df.dropna(inplace=True)  # Drop missing values

# Rename columns for clarity
df.rename(columns={
    "DIM_TIME": "Year",
    "RATE_PER_100_N": "ObesityRate"
}, inplace=True)

# Convert types
df["Year"] = df["Year"].astype(int)
df["ObesityRate"] = df["ObesityRate"].astype(float)

# Drop duplicates if any
df.drop_duplicates(inplace=True)

# Save cleaned data for Power BI
df.to_csv("cleaned_data.csv", index=False)
print("\n✅ Cleaned data saved to 'cleaned_data.csv'")

# Step 5: Exploratory Data Analysis (EDA)
sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Year", y="ObesityRate", marker="o")
plt.title("Obesity Prevalence Over Time in Rwanda (Age 18+)")
plt.xlabel("Year")
plt.ylabel("Obesity Rate (%)")
plt.tight_layout()
plt.savefig("obesity_trend.png")  # Saves chart as image
plt.show()

# Step 6: Forecasting with Linear Regression
X = df[["Year"]]
y = df["ObesityRate"]

model = LinearRegression()
model.fit(X, y)

# Predict for 2026–2030
future_years = pd.DataFrame({"Year": range(2026, 2031)})
predictions = model.predict(future_years)

# Show predictions
print("\n📈 Forecasted Obesity Rates (2026–2030):")
for year, rate in zip(future_years["Year"], predictions):
    print(f"{year}: {rate:.2f}%")

# Plot actual and forecast
plt.figure(figsize=(10, 6))
sns.lineplot(x=df["Year"], y=df["ObesityRate"], label="Actual", marker="o")
sns.lineplot(x=future_years["Year"], y=predictions, label="Forecast", marker="o")
plt.title("Forecasted Obesity Rate in Rwanda (2026–2030)")
plt.xlabel("Year")
plt.ylabel("Obesity Rate (%)")
plt.tight_layout()
plt.savefig("forecast.png")
plt.legend()
plt.show()
