"""Generate a deterministic synthetic store-month jewelry sales dataset."""

from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "jewelry_sales_monthly.csv"
RANDOM_SEED = 42

STORES = [
    ("STR-01", "Mumbai", "West"),
    ("STR-02", "Delhi", "North"),
    ("STR-03", "Bengaluru", "South"),
    ("STR-04", "Chennai", "South"),
    ("STR-05", "Hyderabad", "South"),
    ("STR-06", "Pune", "West"),
    ("STR-07", "Kolkata", "East"),
    ("STR-08", "Ahmedabad", "West"),
    ("STR-09", "Jaipur", "North"),
    ("STR-10", "Kochi", "South"),
]


def build_dataset() -> pd.DataFrame:
    rng = np.random.default_rng(RANDOM_SEED)
    months = pd.date_range("2023-09-01", periods=36, freq="MS")
    rows: list[dict] = []

    for month_number, month in enumerate(months):
        for store_number, (store_id, city, region) in enumerate(STORES, start=1):
            festival = int(month.month in {3, 4, 10, 11})
            digital = rng.uniform(5, 22)
            offline = rng.uniform(3, 13)
            footfall = rng.integers(900, 3501)
            gold_index = 92 + (month.year - 2023) * 4 + rng.uniform(0, 10)
            discount = rng.uniform(2, 12)
            returning = rng.uniform(32, 70)
            inventory = rng.uniform(78, 99)
            average_value = rng.uniform(0.55, 2.0)
            birthdays = rng.integers(15, 85)
            anniversaries = rng.integers(8, 53)
            wedding_leads = rng.integers(4, 34)
            noise = rng.uniform(-12, 12)
            store_effect = store_number * 1.4
            trend = month_number * 0.35

            sales = (
                -10
                + 1.8 * digital
                + 1.1 * offline
                + 0.012 * footfall
                - 0.35 * (gold_index - 100)
                + 2.2 * discount
                + 18 * festival
                + 0.28 * returning
                + 0.18 * inventory
                + 7.0 * average_value
                + 0.06 * birthdays
                + 0.08 * anniversaries
                + 0.22 * wedding_leads
                + store_effect
                + trend
                + noise
            )

            rows.append(
                {
                    "store_id": store_id,
                    "city": city,
                    "region": region,
                    "month": month.strftime("%Y-%m-%d"),
                    "year": month.year,
                    "quarter": f"Q{month.quarter}",
                    "digital_ad_spend_lakh": round(digital, 2),
                    "offline_ad_spend_lakh": round(offline, 2),
                    "store_footfall": int(footfall),
                    "gold_price_index": round(gold_index, 2),
                    "discount_pct": round(discount, 2),
                    "festival_month": festival,
                    "returning_customer_pct": round(returning, 2),
                    "inventory_availability_pct": round(inventory, 2),
                    "avg_transaction_value_lakh": round(average_value, 2),
                    "birthday_customers_count": int(birthdays),
                    "anniversary_customers_count": int(anniversaries),
                    "wedding_leads_count": int(wedding_leads),
                    "noise_lakh": round(noise, 2),
                    "sales_lakh": round(max(sales, 0), 2),
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    dataset = build_dataset()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(OUTPUT_PATH, index=False)
    print(f"Created {OUTPUT_PATH}")
    print(f"Rows: {len(dataset)} | Stores: {dataset['store_id'].nunique()} | Months: {dataset['month'].nunique()}")


if __name__ == "__main__":
    main()


