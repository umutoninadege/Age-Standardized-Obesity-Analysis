# 🥗 Obesity Trend Analysis (18+ Years) – WHO Global Health Observatory

**INSY 8413 – Introduction to Big Data Analytics (Final Exam Project)**
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

### 1. 🧹 Data Cleaning

```python
import pandas as pd
df = pd.read_csv("RELAY_WHS.csv")

# Filter Rwanda + 18+ adults
df_cleaned = df[df["GEO_NAME_SHORT"] == "Rwanda"]
df_cleaned = df_cleaned[df_cleaned["DIM_AGE"] == "Y_GE18"]

# Rename for clarity
df_cleaned.rename(columns={
    "DIM_TIME": "Year",
    "DIM_SEX": "Gender",
    "RATE_PER_100_N": "ObesityRate"
}, inplace=True)

df_cleaned.to_csv("cleaned_data.csv", index=False)
```

### 2. 📈 Exploratory Data Analysis

* Line chart of obesity rate by year
* Trend comparison across genders
* Summary statistics and distribution analysis

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

## 📁 Repository Structure

```
📂 obesity-rwanda-final-project/
├── main.py                  # Python script
├── cleaned_data.csv         # Preprocessed dataset
├── obesity_trend.png        # Line chart image
├── forecast.png             # Forecasted values chart
├── obesity_dashboard.pbix   # Power BI dashboard file
└── README.md                # Project documentation
```

---

## 📊 Key Findings

* Rwanda’s obesity rate among adults (18+) is **steadily increasing**
* Most recent total obesity rate: **4.92%**
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
* Publish dashboard online via **Power BI Service** or **Streamlit**

---

## 🎓 Submission Info

* **Course**: INSY 8413 – Introduction to Big Data Analytics
* **Instructor**: Eric Maniraguha
* **Student**: Umutoni Nadege
* **Final Exam Score**: /40
* **Date**: August 2025

---

## 📬 Contact

* **Email**: [umutoninadege5@gmail.com](mailto:umutoninadege5@gmail.com)
* **GitHub**: [@umutoninadege](https://github.com/umutoninadege)
* **LinkedIn**: [Nadege Umutoni](https://www.linkedin.com/in/nadege-umutoni-456a61318)

---

## 🙏 Reflective Verse

> “Whatever you do, work at it with all your heart, as working for the Lord…”
> — *Colossians 3:23*

This project reflects not only technical growth but also a commitment to meaningful work that supports public health.
