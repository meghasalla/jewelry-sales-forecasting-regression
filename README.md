# Jewelry Sales Prediction Using Regression

## Project Overview

This portfolio project explores how regression can predict monthly jewelry sales from advertising, customer footfall, gold prices, discounts, festivals, repeat customers, inventory availability, and customer occasions.

It is designed to demonstrate both machine-learning fundamentals and business-strategy thinking.

> **Data disclaimer:** Use synthetic or authorized data only. Do not present the dataset as real data from Tanishq, Malabar, or another jewelry company.

## Business Problem

Jewelry retailers must plan marketing budgets, inventory, promotions, staffing, and customer engagement before future demand is known. Weak forecasts can cause excess inventory, stockouts, inefficient advertising, missed seasonal demand, and unrealistic store targets.

The central question is:

> Can historical business drivers estimate monthly jewelry sales and explain which factors have the strongest relationship with revenue?

## Proposed Solution

Build an interpretable multiple linear regression baseline using one row per store per month. Evaluate it on future, unseen months and translate the results into recommendations for store, marketing, inventory, and finance teams.

After the baseline, compare a tree-based model if nonlinear relationships appear important. Keep linear regression as the explainability benchmark.

## Target Users

- Retail leadership and finance teams
- Store managers
- Marketing and CRM teams
- Inventory and merchandising teams
- AI and business strategy consultants

## Dataset Design

Use one row per **store per month**.

### Target

| Field | Meaning | Unit |
|---|---|---|
| `sales_lakh` | Total monthly jewelry sales | Lakh INR |

### Candidate Features

| Feature | Meaning |
|---|---|
| `store_id` | Unique store identifier |
| `month` | Month represented by the row |
| `region` | Store region |
| `digital_ad_spend_lakh` | Digital advertising spend |
| `offline_ad_spend_lakh` | Offline advertising spend |
| `store_footfall` | Number of store visitors |
| `gold_price_index` | Relative gold price level |
| `discount_pct` | Average discount offered |
| `festival_month` | Major demand event indicator |
| `returning_customer_pct` | Share of returning customers |
| `inventory_availability_pct` | Desired inventory availability |
| `avg_transaction_value_lakh` | Average order value |
| `birthday_customers_count` | Customers with birthdays that month |
| `anniversary_customers_count` | Customers with anniversaries that month |
| `wedding_leads_count` | Active wedding-related leads |

## Why Regression?

Regression is suitable because monthly sales is a continuous number. Multiple linear regression is a strong first model because it is easy to explain, fast to train, and useful as a transparent baseline.

Regression coefficients show association, not automatic causation. A positive coefficient does not prove that changing a feature will create the predicted increase.

## Project Workflow

1. Define the business decision and forecast horizon.
2. Prepare the store-month dataset.
3. Check types, missing values, duplicates, and unrealistic values.
4. Perform exploratory data analysis.
5. Study correlations and multicollinearity.
6. Create a time-based training and testing split.
7. Establish a simple mean or previous-month baseline.
8. Train multiple linear regression.
9. Evaluate predictions and residuals.
10. Compare with a regularized or tree-based model if justified.
11. Convert results into actions, risks, and pilot recommendations.

## Model Evaluation

| Metric | Business meaning |
|---|---|
| MAE | Average absolute prediction error |
| RMSE | Error metric that penalizes large misses more strongly |
| R-squared | Share of sales variation explained by the model |
| Residual plots | Reveal bias, patterns, and changing error variance |
| Baseline comparison | Confirms whether the model beats a simple rule |

## Bias and Variance

- **High bias:** Training and testing performance are both weak; meaningful features or a more flexible model may be needed.
- **High variance:** Training is strong but testing is weak; simplify, regularize, or add better data.
- **Data leakage:** Future information appears in training inputs; prevent it with a time-based split and feature-availability checks.

## Recommended Structure

```text
Workspace/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_business_and_data_understanding.ipynb
│   └── 02_sales_regression_model.ipynb
├── src/
│   ├── data_preparation.py
│   └── train_model.py
├── models/
├── reports/
│   └── figures/
├── .venv/
├── .gitignore
├── requirements.txt
└── README.md
```

Do not upload `.venv` to GitHub.

## License

This project is released under the MIT License. See `LICENSE` for details.

## Environment Setup

In Command Prompt:

```bat
cd /d "C:\Users\Lenovo\Desktop\Workspace"
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pip list
```

When finished:

```bat
deactivate
```

## Installed Libraries

- pandas — tabular data preparation
- NumPy — numerical operations
- Matplotlib — foundational plotting
- Seaborn — statistical visualization
- scikit-learn — preprocessing, regression, and evaluation
- Statsmodels — statistical regression diagnostics
- OpenPyXL — Excel access
- Joblib — model persistence
- IPython kernel — notebook execution in Visual Studio Code

## Expected Business Deliverables

- Documented problem and modeling objective
- Data dictionary and quality summary
- Exploratory charts with business interpretations
- Regression baseline and evaluation scorecard
- Coefficient and residual analysis
- Recommendations for marketing, inventory, and store planning
- Limitations, risks, assumptions, and pilot plan

## Verified Baseline Result

The reusable regression script was successfully tested on the synthetic dataset using the latest six months as the holdout period:

| Metric | Result |
|---|---:|
| Model MAE | 6.198 lakh INR |
| Model RMSE | 7.689 lakh INR |
| Model R-squared | 0.815 |
| Mean-baseline MAE | 14.613 lakh INR |

These results validate the technical workflow on synthetic data; they do not represent performance for a real jewelry retailer.

## Interview Story

Explain the work in this order: business problem, decision supported, data design, interpretable model, future-period evaluation, business insight, risks, and pilot next step. Emphasize that the model supports decisions rather than replacing managers.

## Current Status

- [x] Virtual environment created
- [x] Required libraries installed
- [x] `requirements.txt` created
- [x] `README.md` created
- [x] Folder structure created
- [x] Synthetic dataset prepared
- [ ] Exploratory analysis completed
- [x] Regression model trained
- [x] Evaluation documented
- [ ] Recommendations completed
- [ ] GitHub repository published

