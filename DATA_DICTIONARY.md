# Data Dictionary

The dataset uses one row per store per month. All values are synthetic and intended only for learning and portfolio demonstration.

| Column | Role | Type | Unit / values | Business meaning | Expected range |
|---|---|---|---|---|---|
| `store_id` | Identifier | Text | `STR-01` to `STR-10` | Unique jewelry store | 10 stores |
| `city` | Input | Category | Indian city | Store market | Defined store list |
| `region` | Input | Category | North, South, East, West | Store region | Four categories |
| `month` | Time key | Date | First day of month | Month represented by the row | Sep 2023–Aug 2026 |
| `year` | Time key | Integer | Calendar year | Supports yearly summaries | 2023–2026 |
| `quarter` | Time key | Category | Q1–Q4 | Supports quarterly summaries | Four categories |
| `digital_ad_spend_lakh` | Input | Decimal | Lakh INR | Digital marketing investment | 5–22 |
| `offline_ad_spend_lakh` | Input | Decimal | Lakh INR | Print, outdoor, radio, and local promotions | 3–13 |
| `store_footfall` | Input | Integer | Visitors | Monthly visitors | 900–3,500 |
| `gold_price_index` | Input | Decimal | Index | Synthetic relative gold-price level | Approximately 92–114 |
| `discount_pct` | Input | Decimal | Percentage points | Average discount in the month | 2–12 |
| `festival_month` | Input | Binary | 0 or 1 | Whether a major demand event occurs | 0–1 |
| `returning_customer_pct` | Input | Decimal | Percentage points | Share of buyers who returned | 32–70 |
| `inventory_availability_pct` | Input | Decimal | Percentage points | Desired inventory available for sale | 78–99 |
| `avg_transaction_value_lakh` | Input | Decimal | Lakh INR | Average transaction value | 0.55–2.00 |
| `birthday_customers_count` | Input | Integer | Customers | Contactable birthday customers | 15–84 |
| `anniversary_customers_count` | Input | Integer | Customers | Contactable anniversary customers | 8–52 |
| `wedding_leads_count` | Input | Integer | Leads | Active wedding-related opportunities | 4–33 |
| `noise_lakh` | Simulation only | Decimal | Lakh INR | Fixed random variation in synthetic generation | -12–12 |
| `sales_lakh` | Target | Decimal | Lakh INR | Total monthly jewelry sales to predict | Non-negative |

## Modeling Notes

- Do not use `noise_lakh` as a model input; it exists only to make the synthetic target less perfect.
- Use a time-based split. The latest six months are the recommended test period.
- Treat `store_id`, `city`, and `region` as categorical variables.
- Coefficients show association, not proof of causation.
- Check for multicollinearity among advertising, footfall, and event-related features.


