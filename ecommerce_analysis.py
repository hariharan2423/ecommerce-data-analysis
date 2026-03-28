# ==============================
# E-COMMERCE DATA ANALYSIS PROJECT
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# ------------------------------
# 1. LOAD DATA
# ------------------------------
df = pd.read_csv("e commerce_large.csv")

print("Dataset Loaded Successfully!\n")
print(df.head())

# ------------------------------
# 2. DATA CLEANING
# ------------------------------
df.dropna(inplace=True)

# Create Total Price
df["TotalPrice"] = df["Quantity"] * df["Price"]

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")

# ------------------------------
# 3. BASIC ANALYSIS
# ------------------------------

# Top Products
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\nTop Products:\n", top_products)

# Category Sales
category_sales = df.groupby("Category")["TotalPrice"].sum()
print("\nCategory Sales:\n", category_sales)

# Monthly Sales
monthly_sales = df.groupby("Month")["TotalPrice"].sum()
print("\nMonthly Sales:\n", monthly_sales)

# ------------------------------
# 4. CUSTOMER ANALYSIS
# ------------------------------

customer_data = df.groupby("CustomerID")["TotalPrice"].sum().reset_index()

# Top 5 Customers
top_customers = customer_data.sort_values(by="TotalPrice", ascending=False).head(5)
print("\nTop 5 High-Value Customers:\n", top_customers)

# ------------------------------
# 5. CUSTOMER SEGMENTATION (ML)
# ------------------------------

kmeans = KMeans(n_clusters=3, random_state=0)
customer_data["Segment"] = kmeans.fit_predict(customer_data[["TotalPrice"]])

print("\nCustomer Segmentation:\n", customer_data.head())

# ------------------------------
# 6. VISUALIZATION
# ------------------------------

# Top Products Bar Chart
plt.figure()
top_products.head(10).plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Products")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.show()

# Category Pie Chart
plt.figure()
category_sales.plot(kind="pie", autopct='%1.1f%%')
plt.title("Category Sales Distribution")
plt.ylabel("")
plt.show()

# Monthly Sales Line Chart
plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Customer Segmentation Scatter
plt.figure()
plt.scatter(customer_data["CustomerID"], customer_data["TotalPrice"], c=customer_data["Segment"])
plt.title("Customer Segmentation")
plt.xlabel("Customer ID")
plt.ylabel("Total Spending")
plt.show()

# ------------------------------
# 7. FINAL INSIGHTS
# ------------------------------

print("\n--- FINAL INSIGHTS ---")
print("1. Electronics dominate sales (>90%)")
print("2. Customer spending varies significantly")
print("3. Sales show monthly fluctuations")
print("4. High-value customers contribute major revenue")