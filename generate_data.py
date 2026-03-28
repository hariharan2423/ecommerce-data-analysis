import pandas as pd
import random
from datetime import datetime, timedelta

# Sample data
customers = list(range(1000, 1100))
products = ["Laptop", "Mobile", "Headphones", "Shoes", "T-shirt", "Watch", "Backpack", "Keyboard", "Mouse", "Tablet"]

categories = {
    "Laptop": "Electronics",
    "Mobile": "Electronics",
    "Headphones": "Electronics",
    "Keyboard": "Electronics",
    "Mouse": "Electronics",
    "Tablet": "Electronics",
    "Shoes": "Fashion",
    "T-shirt": "Fashion",
    "Watch": "Accessories",
    "Backpack": "Accessories"
}

prices = {
    "Laptop": 55000,
    "Mobile": 20000,
    "Headphones": 1500,
    "Keyboard": 1200,
    "Mouse": 500,
    "Tablet": 15000,
    "Shoes": 3000,
    "T-shirt": 700,
    "Watch": 2500,
    "Backpack": 1200
}

# Generate dataset
data = []
start_date = datetime(2024, 1, 1)

for _ in range(10000):
    product = random.choice(products)
    quantity = random.randint(1, 5)
    date = start_date + timedelta(days=random.randint(0, 180))

    data.append([
        random.choice(customers),
        product,
        categories[product],
        quantity,
        prices[product],
        date.strftime("%Y-%m-%d")
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=["CustomerID", "Product", "Category", "Quantity", "Price", "Date"])

# Save CSV file
df.to_csv("e commerce_large.csv", index=False)

print("Dataset created successfully!")