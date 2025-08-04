# Age-Standardized-Obesity-Analysis
Obesity trend analysis worldwide (18+) with focus on Rwanda using WHO data — Python + Power BI

# 🥗 Obesity Trend Analysis (18+ Years) – WHO Global Health Observatory

**INSY 8413 – Introduction to Big Data Analytics (Final Exam Project)**  
This project presents a comprehensive analysis of the **age-standardized prevalence of obesity among adults (18+ years)**, using data from the **WHO Global Health Observatory**. It focuses on **Rwanda**, with optional global comparison, and combines **Python analytics** and an **interactive Power BI dashboard** to derive actionable health insights.

---

## 🏥 Sector: Health  
**Focus Area**: Non-communicable diseases, adult obesity, gender-based analysis, public health forecasting

---

## 📊 Project Objectives

🎯 **Goals:**
- Track historical trends in obesity prevalence (1990–latest)
- Compare obesity levels by gender (MALE, FEMALE, TOTAL)
- Predict future obesity rates for Rwanda (2026–2030)
- Build an interactive Power BI dashboard for decision support

---

## 🌐 Dataset Information

- **Source**: [WHO Global Health Observatory](https://data.who.int/indicators/i/C6262EC/BEFA58B?m49=646)
- **Scope**: Global (filtered for Rwanda)
- **Age Group**: 18+ (DIM_AGE = Y_GE18)
- **Columns**: Year, Country, Gender, Obesity Rate, Confidence Intervals
- **Status**: Structured CSV, required preprocessing

---

## 🛠️ Tools & Technologies

| Tool           | Purpose                         |
|----------------|----------------------------------|
| Python (VS Code) | Data cleaning, EDA, forecasting |
| Pandas, Seaborn, Scikit-learn | Visualization & regression modeling |
| Power BI       | Dashboard & interactive reporting |
| GitHub         | Version control & documentation  |

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

