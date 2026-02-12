# Sales Data Analysis Project

## Overview

This project analyzes retail sales data to identify key business insights, including revenue trends by city, customer spending behavior, and product performance.

## Project Structure

- `data/raw/`: Original sales dataset.
- `data/processed/`: Cleaned data used for analysis.
- `notebooks/`: Jupyter Notebook containing Graph 1 to Graph 4.
- `src/`: Python scripts for data cleaning.

## Key Insights

1. **City Performance:** New York is the leading branch in terms of revenue.
2. **Customer Loyalty:** Members contribute more significantly to sales than normal customers.
3. **Product Trends:** 'Food and Beverages' is the most popular category.
4. **Price Elasticity:** Unit price shows a stable relationship with quantity sold.

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Run cleaning script: `python src/data_cleaning.py`
3. View analysis: Open `notebooks/analysis.ipynb`

##Visualization

- Graph 1:Total Sales Revenue by City
  ![City Revenue](../images/graph1_city_revenue.png)
  - Top Market: New York leads in total revenue, suggesting it is the most profitable branch.

  - Market Stability: Revenue is distributed relatively evenly across all cities, showing a balanced business presence.

_Insight: New York shows the highest revenue among all branches._

- Graph 2: Customer Spending Behavior (Member vs. Normal)
  ![Customer Behavior](../images/graph2_customer_spending.png)
  - Loyalty Impact: Members generally contribute more to the total revenue compared to Normal customers.

  - Gender Trends: Female members in certain branches show a higher spending pattern, which is a key insight for targeted marketing.

  _Insight: Members spend more than regular customers, especially in the Female segment._

- Graph 3: Product Category Performance
  ![Product Performance](../images/graph3_product_performance.png)
  - Best Sellers: Food and Beverages and Fashion Accessories are the top-performing categories.

  - Inventory Optimization: Low-performing categories should be reviewed for stock reduction or promotional discounts.

  _Insight: Food and Beverages is the most profitable category._

- Graph 4: Unit Price vs. Quantity (Correlation)
  ![Price Correlation](../images/graph4_price_correlation.png)
  - Price Sensitivity: There is a wide distribution of purchases across all price points, suggesting customers are not highly sensitive to unit prices within this range.

  - Bulk Buying: High-quantity purchases occur even for mid-to-high priced items, indicating strong purchasing power among the customer base.

  _Insight: Customers are less sensitive to price changes for essential categories._
