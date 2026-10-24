#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Project Title

#**Basic Linear Regression: Association Between Patient Age and Billing Amount**

## Centering the Explanatory Variable

#My primary explanatory variable is **patient age**, which is quantitative. Therefore, I centered Age by subtracting the sample mean from each observation.

#The original mean age was approximately **51.54 years**.

#After centering:

#**Mean of centered Age = 0.00**

#This confirms that the explanatory variable was centered correctly.

### Python Syntax

#```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import glob
import os

# ============================================================
# FIND AND LOAD HEALTHCARE DATASET
# ============================================================

csv_files = glob.glob("**/*.csv", recursive=True)

data_file = None

for file in csv_files:
    if os.path.basename(file).lower() == "healthcare_dataset.csv":
        data_file = file
        break

if data_file is None:
    for file in csv_files:
        if "healthcare" in os.path.basename(file).lower():
            data_file = file
            break

if data_file is None:
    raise FileNotFoundError(
        "healthcare_dataset.csv was not found. "
        "Please upload the healthcare dataset first."
    )

data = pd.read_csv(data_file, low_memory=False)

print("=" * 70)
print("BASIC LINEAR REGRESSION")
print("AGE PREDICTING BILLING AMOUNT")
print("=" * 70)

# ============================================================
# DATA MANAGEMENT
# ============================================================

# Convert Age to numeric
data["Age_Clean"] = pd.to_numeric(
    data["Age"],
    errors="coerce"
)

# Code impossible ages as missing
data.loc[
    (data["Age_Clean"] < 0) |
    (data["Age_Clean"] > 120),
    "Age_Clean"
] = np.nan

# Convert Billing Amount to numeric
data["Billing_Clean"] = pd.to_numeric(
    data["Billing Amount"],
    errors="coerce"
)

# Code zero or negative billing amounts as missing
data.loc[
    data["Billing_Clean"] <= 0,
    "Billing_Clean"
] = np.nan

# Keep complete observations
regression_data = data[
    ["Age_Clean", "Billing_Clean"]
].dropna().copy()

print("\nNumber of valid observations:",
      len(regression_data))

# ============================================================
# CENTER AGE
# ============================================================

age_mean = regression_data["Age_Clean"].mean()

regression_data["Age_Centered"] = (
    regression_data["Age_Clean"] - age_mean
)

print("\nCENTERING CHECK")
print("-" * 70)

print(
    "Original mean Age:",
    round(age_mean, 2)
)

print(
    "Mean of centered Age:",
    round(regression_data["Age_Centered"].mean(), 6)
)

# ============================================================
# LINEAR REGRESSION
# ============================================================

X = sm.add_constant(
    regression_data["Age_Centered"]
)

Y = regression_data["Billing_Clean"]

model = sm.OLS(Y, X).fit()

print("\n" + "=" * 70)
print("LINEAR REGRESSION RESULTS")
print("=" * 70)

print(model.summary())

# ============================================================
# DISPLAY IMPORTANT RESULTS
# ============================================================

print("\nREGRESSION COEFFICIENTS")
print("-" * 70)

print(
    "Intercept:",
    round(model.params["const"], 2)
)

print(
    "Age coefficient:",
    round(model.params["Age_Centered"], 2)
)

print(
    "Age p-value:",
    round(model.pvalues["Age_Centered"], 4)
)

print(
    "R-squared:",
    round(model.rsquared, 6)
)

print("\nANALYSIS COMPLETE")
#```

## Output

### Centering Check
#**Number of valid observations: 55,392**

#**Original mean Age = 51.54 years**

#**Mean of centered Age = approximately 0.000000**

#Therefore, the Age variable was successfully centered.

## Linear Regression Results

#The estimated regression equation was:

#**Billing Amount = $25,590.08 − $2.72 × Centered Age**

### Regression Statistics

#| Statistic | Result |
#|---|---:|
#| Intercept | $25,590.08 |
#| Age regression coefficient | -2.72 |
#| Age p-value | 0.3767 |
#| R² | 0.000014 |
#| N | 55,392 |

#The 95% confidence interval for the Age coefficient was approximately **-8.74 to 3.31**.

## Interpretation

#A basic linear regression analysis was conducted to determine whether **patient Age was associated with Billing Amount**.

#The regression coefficient for centered Age was **B = -2.72, p = .377**. This means that for each additional year of age, the model predicts an average decrease of approximately **$2.72 in billing amount**.

#However, this association was **not statistically significant** because the p-value of .377 is greater than the .05 significance level. Therefore, I fail to reject the null hypothesis that there is no linear association between patient age and billing amount.

#The model had an **R² of approximately 0.000014**, meaning Age explained only about **0.0014% of the variability in Billing Amount**. This indicates that patient age alone provides essentially no useful explanation of differences in billing amounts within this dataset.

#Because Age was centered at its mean, the intercept of **$25,590.08** represents the predicted billing amount for a patient at the average age of approximately **51.54 years**.

## Summary

#The results of the basic linear regression indicated that **patient Age was not significantly associated with Billing Amount, B = -2.72, p = .377**.

#Although the coefficient was slightly negative, the effect was extremely small and statistically nonsignificant. Therefore, patient age does not appear to be a useful individual predictor of billing amount in this synthetic healthcare dataset.

## URL

#**Paste the URL of your published blog entry here.**

