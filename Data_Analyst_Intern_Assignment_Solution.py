
# Supertails - Data Analyst Intern Assignment  
# Mehtab Alam

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Datasets
# -----------------------------

events = pd.read_csv("events_data.csv")
orders = pd.read_csv("orders_data.csv")
customers = pd.read_csv("customers_data.csv")

# -----------------------------
# 2. Data Cleaning & Preparation 
# -----------------------------

# Convert date columns
events['event_date'] = pd.to_datetime(events['event_date'], format='%Y%m%d')
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Remove duplicates
events = events.drop_duplicates()
orders = orders.drop_duplicates()
customers = customers.drop_duplicates()

# Filter valid orders
orders = orders[orders['order_status'] == 'valid']

# Ensure consistent datatypes for joins
events['user_id'] = events['user_id'].astype(str)
orders['customer_id'] = orders['customer_id'].astype(str)
customers['customer_id'] = customers['customer_id'].astype(str)

print("Data Cleaning Completed Successfully!")

# -----------------------------
# 3. User Engagement → Purchase Funnel
# -----------------------------

# Unique users with events
users_with_events = events['user_id'].nunique()

# Users with at least one valid order
users_with_orders = orders['customer_id'].nunique()

# Conversion rate
conversion_rate = users_with_orders / users_with_events

print("\nFunnel Metrics Summary")
print("-----------------------")
print("Users with Events:", users_with_events)
print("Users with Valid Orders:", users_with_orders)
print("Conversion Rate: {:.2%}".format(conversion_rate))

# -----------------------------
# 4. Daily Trend Visualization
# -----------------------------

daily_active = events.groupby('event_date')['user_id'].nunique()
daily_orders = orders.groupby('order_date')['customer_id'].nunique()

plt.figure()
plt.plot(daily_active.index, daily_active.values)
plt.title("Daily Active Users")
plt.xlabel("Date")
plt.ylabel("Active Users")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_active_users.png")
plt.close()

plt.figure()
plt.plot(daily_orders.index, daily_orders.values)
plt.title("Daily Ordering Customers")
plt.xlabel("Date")
plt.ylabel("Ordering Customers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_ordering_customers.png")
plt.close()

print("\nTime-series charts saved as PNG files.")

# -----------------------------
# 5. Customer Behavior Insight
# -----------------------------

merged = orders.merge(customers, on='customer_id', how='left')

# Revenue by Acquisition Channel
channel_revenue = merged.groupby('acq_channel')['net_sales'].sum().sort_values(ascending=False)

plt.figure()
channel_revenue.plot(kind='bar')
plt.title("Revenue by Acquisition Channel")
plt.xlabel("Acquisition Channel")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("revenue_by_channel.png")
plt.close()

print("\nBar chart saved as revenue_by_channel.png")

# City with highest Average Order Value
city_aov = merged.groupby('city')['net_sales'].mean().sort_values(ascending=False)

print("\nTop City by Average Order Value:")
print(city_aov.head(1))

print("\nAnalysis Completed Successfully!")
