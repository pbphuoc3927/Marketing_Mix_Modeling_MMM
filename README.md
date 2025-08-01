# 📊 Marketing Mix Modeling (MMM)

## 🧠 Project Overview

This project demonstrates how to use **Marketing Mix Modeling (MMM)** techniques to analyze the impact of different marketing channels on revenue. Using simulated weekly marketing spend data, we applied regression-based methods to:

- Quantify the ROI of each marketing channel
- Identify underperforming vs high-performing channels
- Recommend optimized budget allocation based on ROI

---

## 📈 Objectives

- Model the relationship between marketing spend and weekly revenue
- Calculate ROI for each channel
- Simulate optimized budget allocation under the same total spend constraint
- Generate actionable business insights and strategic recommendations

---

## 🧪 Dataset

- **Source**: Synthetic data (1000 weekly records)
- **Features**:
  - `week`: weekly timestamp
  - `tv_spend`: weekly spend on TV ads
  - `facebook_spend`: spend on Facebook
  - `search_spend`: spend on search marketing
  - `other_spend`: other miscellaneous spend
  - `revenue`: weekly total revenue

---

## 🔧 Project Structure

```

Marketing\_Mix\_Modeling\_MMM/
│
├── data/
│   └── marketing\_weekly\_spend.csv
│
├── notebooks/
│   └── analysis.ipynb            
│
├── scripts/
│   └── generate_mock_data.py   
│ 
├── outputs/
│   ├── figures/                         
│   ├── reports/                         
│   └── models/                         
│
├── scripts/
│   └── generate\_mock\_data.py            
│
├── .gitignore
├── requirements.txt
└── README.md

````

---

## 📌 Key Steps

1. **Mock Data Generation**  
   Simulated weekly marketing spend and revenue using controlled linear relationships and random noise.

2. **Exploratory Data Analysis**  
   Visualized distributions, correlation matrix, and summary statistics.

3. **Modeling**  
   Applied **Ordinary Least Squares (OLS)** linear regression to estimate revenue as a function of channel spend.

4. **Multicollinearity Check**  
   Verified VIF values to ensure stable regression coefficients.

5. **ROI Calculation & Budget Optimization**  
   - Estimated ROI for each channel
   - Reallocated total budget based on ROI proportions

6. **Insight Generation**  
   - Summarized top and underperforming channels
   - Proposed reallocation strategy with a clear business narrative

---

## 🔍 Results & Insights

Example output from regression-based ROI analysis:

- 📈 **Top ROI Channel**: `search_spend`
- 🔻 **Underperforming**: `other_spend`
- 🧮 Reallocation Suggestion: Shift more budget to `facebook_spend` and `search_spend`

> 💡 All strategic insights are stored in:  
> `outputs/reports/summary_insights.txt`

---

## 🛠️ Tools Used

- `Python`
- `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`
- `Statsmodels` for regression and VIF
- `Scikit-learn` for preprocessing

---

## 📦 Installation

```bash
pip install -r requirements.txt
````

---

## 🤖 Author

Developed by \Pham Ba Phuoc, 2025
This project is part of a portfolio focused on marketing analytics & data-driven business strategy.