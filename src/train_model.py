"""Train and evaluate an interpretable jewelry sales regression baseline."""

from pathlib import Path

import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "jewelry_sales_monthly.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "linear_regression.joblib"
FIGURE_PATH = PROJECT_ROOT / "reports" / "figures" / "actual_vs_predicted.png"

TARGET = "sales_lakh"
CATEGORICAL_FEATURES = ["store_id", "region"]
NUMERIC_FEATURES = [
    "digital_ad_spend_lakh",
    "offline_ad_spend_lakh",
    "store_footfall",
    "gold_price_index",
    "discount_pct",
    "festival_month",
    "returning_customer_pct",
    "inventory_availability_pct",
    "avg_transaction_value_lakh",
    "birthday_customers_count",
    "anniversary_customers_count",
    "wedding_leads_count",
]
FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES


def load_data() -> pd.DataFrame:
    data = pd.read_csv(DATA_PATH, parse_dates=["month"])
    return data.sort_values(["month", "store_id"]).reset_index(drop=True)


def build_model() -> Pipeline:
    numeric_pipeline = Pipeline(
        [("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]
    )
    categorical_pipeline = Pipeline(
        [
            ("impute", SimpleImputer(strategy="most_frequent")),
            ("encode", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocessing = ColumnTransformer(
        [
            ("numeric", numeric_pipeline, NUMERIC_FEATURES),
            ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
        ]
    )
    return Pipeline([("preprocessing", preprocessing), ("regression", LinearRegression())])


def main() -> None:
    data = load_data()
    test_months = sorted(data["month"].unique())[-6:]
    train = data[~data["month"].isin(test_months)]
    test = data[data["month"].isin(test_months)]

    model = build_model()
    model.fit(train[FEATURES], train[TARGET])
    predictions = model.predict(test[FEATURES])

    mean_baseline = [train[TARGET].mean()] * len(test)
    results = pd.Series(
        {
            "Model MAE": mean_absolute_error(test[TARGET], predictions),
            "Model RMSE": mean_squared_error(test[TARGET], predictions) ** 0.5,
            "Model R2": r2_score(test[TARGET], predictions),
            "Mean baseline MAE": mean_absolute_error(test[TARGET], mean_baseline),
        }
    )
    print(results.round(3).to_string())

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    plt.figure(figsize=(7, 5))
    plt.scatter(test[TARGET], predictions, alpha=0.75)
    limits = [min(test[TARGET].min(), predictions.min()), max(test[TARGET].max(), predictions.max())]
    plt.plot(limits, limits, "--", color="black", label="Perfect prediction")
    plt.xlabel("Actual sales (lakh INR)")
    plt.ylabel("Predicted sales (lakh INR)")
    plt.title("Actual vs Predicted Monthly Jewelry Sales")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURE_PATH, dpi=160)
    print(f"Saved model: {MODEL_PATH}")
    print(f"Saved chart: {FIGURE_PATH}")


if __name__ == "__main__":
    main()

