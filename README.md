# 🥗 Obesity Trend Analysis (18+ Years) – WHO Global Health Observatory


This project presents a comprehensive analysis of the **age-standardized prevalence of obesity among adults (18+ years)**, using data from the **WHO Global Health Observatory**. It focuses on **Rwanda**, with optional global comparison, and combines **Python analytics** and an **interactive Power BI dashboard** to derive actionable health insights.

---

## 🏥 Sector: Health

**Focus Area**: Non-communicable diseases, adult obesity, gender-based analysis, public health forecasting

---

## 📊 Project Objectives

🎯 **Goals:**

* Track historical trends in obesity prevalence (1990–latest)
* Compare obesity levels by gender (MALE, FEMALE, TOTAL)
* Predict future obesity rates for Rwanda (2026–2030)
* Build an interactive Power BI dashboard for decision support

---

## 🌐 Dataset Information

* **Source**: [WHO Global Health Observatory](https://data.who.int/indicators/i/C6262EC/BEFA58B?m49=646)
* **Scope**: Global (filtered for Rwanda)
* **Age Group**: 18+ (DIM\_AGE = Y\_GE18)
* **Columns**: Year, Country, Gender, Obesity Rate, Confidence Intervals
* **Status**: Structured CSV, required preprocessing

---

## 🛠️ Tools & Technologies

| Tool                          | Purpose                             |
| ----------------------------- | ----------------------------------- |
| Python (VS Code)              | Data cleaning, EDA, forecasting     |
| Pandas, Seaborn, Scikit-learn | Visualization & regression modeling |
| Power BI                      | Dashboard & interactive reporting   |
| GitHub                        | Version control & documentation     |

---

## 🔬 Methodology
### 1. Load Dataset
Loaded the dataset using Pandas
```python

df = pd.read_csv("RELAY_WHS.csv")

# Step 3: Show Basic Info
print("\n--- Dataset Info ---")
print(df.info())
print(df.head())

```
### 2. 🧹 Data Cleaning and Rename columns

```python
import pandas as pd
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

```

### 2. 📈 Exploratory Data Analysis

* Line chart of obesity rate by year
* Trend comparison across genders
* Summary statistics and distribution analysis
* ```python
  import pandas as pd
  sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Year", y="ObesityRate", marker="o")
plt.title("Obesity Prevalence Over Time in Rwanda (Age 18+)")
plt.xlabel("Year")
plt.ylabel("Obesity Rate (%)")
plt.tight_layout()
plt.savefig("obesity_trend.png")  # Saves chart as image
plt.show()
```
### 3. 🤖 Forecasting

Used **Linear Regression** to predict obesity rates for 2026–2030:

```python
from sklearn.linear_model import LinearRegression
import pandas as pd

X = df_cleaned[["Year"]]
y = df_cleaned["ObesityRate"]

model = LinearRegression()
model.fit(X, y)

# Predict future years
future = pd.DataFrame({"Year": range(2026, 2031)})
forecast = model.predict(future)
```

### 4. 📊 Power BI Dashboard Features

* **KPI Card**: Shows the latest obesity rate (e.g., 4.92%)
* **Slicer**: Gender filter (MALE, FEMALE, TOTAL)
* **Line Chart**: Visualizes obesity trends over time
* **Forecast Visual**: 5-year prediction with confidence intervals
* **Smart Narrative** *(optional)*: Automatically generates insights

---



## 📊 Key Findings

* Rwanda’s obesity rate among adults (18+) is **steadily increasing**
* Most recent total obesity rate in Rwanda: **4.92%**
* * Most recent total obesity rate worldwide: **80.39%**
* Male vs. Female differences observed in various years
* Forecast suggests a **continued upward trend** through 2030

---

## 💡 Recommendations

* 🧠 Launch awareness programs targeting rising adult obesity
* 📊 Prioritize **female-focused** health education campaigns
* 📈 Track obesity as a risk factor for other **NCDs**

---

## 🌟 Future Work

* Compare trends with regional neighbors (e.g., Kenya, Uganda)
* Add dietary/lifestyle data for deeper insights
* Publish dashboard online via **Power BI Service** 







This project reflects not only technical growth but also a commitment to meaningful work that supports public health.
