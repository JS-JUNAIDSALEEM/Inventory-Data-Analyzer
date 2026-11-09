
import pandas as pd
import numpy as np
import os

# Inventory Dataset
products = [
    {"ProductID": 101,   "ProductName": "Laptop",        "Category": "Electronics",   "Price": 85000,     "Quantity": 8},
    {"ProductID": 102,   "ProductName": "Mouse",         "Category": "Accessories",   "Price": 1200,      "Quantity": 35},
    {"ProductID": 103,   "ProductName": "Keyboard",      "Category": "Accessories",   "Price": 2500,      "Quantity": 20},
    {"ProductID": 104,   "ProductName": "Monitor",       "Category": "Electronics",   "Price": 32000,     "Quantity": 12},
    {"ProductID": 105,   "ProductName": "Printer",       "Category": "Electronics",   "Price": 28000,     "Quantity": 6},
    {"ProductID": 106,   "ProductName": "Office Chair",  "Category": "Furniture",     "Price": 18000,     "Quantity": 15},
    {"ProductID": 107,   "ProductName": "Desk",          "Category": "Furniture",     "Price": 25000,     "Quantity": 9},
    {"ProductID": 108,   "ProductName": "USB Drive",     "Category": "Accessories",   "Price": 1500,      "Quantity": 50},
    {"ProductID": 109,   "ProductName": "Headphones",    "Category": "Electronics",   "Price": 4500,      "Quantity": 18},
    {"ProductID": 110,   "ProductName": "Webcam",        "Category": "Electronics",   "Price": 6500,      "Quantity": 7},
    {"ProductID": 111,   "ProductName": "Notebook",      "Category": "Stationery",    "Price": 250,       "Quantity": 100},
    {"ProductID": 112,   "ProductName": "Pen Pack",      "Category": "Stationery",    "Price": 300,       "Quantity": 75},
    {"ProductID": 113,   "ProductName": "Bookshelf",     "Category": "Furniture",     "Price": 14000,     "Quantity": 5},
    {"ProductID": 114,   "ProductName": "Tablet",        "Category": "Electronics",   "Price": 45000,     "Quantity": 10},
    {"ProductID": 115,   "ProductName": "Paper Pack",    "Category": "Stationery",    "Price": 600,       "Quantity": 40}
]


# Create DataFrame
df = pd.DataFrame(products)

print("====== INVENTORY DATA ANALYZER ======")

# 1. Display Inventory Dataset
print("\n--- Complete Inventory Data ---")
print(df.to_string(index=False))


# 2. Basic Inventory Information
total_products = len(df)
total_stock = df["Quantity"].sum()
total_inventory_value = (df["Price"] * df["Quantity"]).sum()

print("\n--- Inventory Information ---")
print("Total Products:", total_products)
print("Total Available Stock:", total_stock)
print("Total Inventory Value:", total_inventory_value)


# 3. Find Most Expensive Product
expensive_product = df.loc[df["Price"].idxmax()]

print("\n--- Most Expensive Product ---")
print("Product Name:", expensive_product["ProductName"])
print("Price:", expensive_product["Price"])


# 4. Find Cheapest Product
cheapest_product = df.loc[df["Price"].idxmin()]

print("\n--- Cheapest Product ---")
print("Product Name:", cheapest_product["ProductName"])
print("Price:", cheapest_product["Price"])


# 5. Find Low Stock Products
low_stock = df[df["Quantity"] <= 10]

print("\n--- Low Stock Products ---")
print(low_stock.to_string(index=False))


# 6. Calculate Average Product Price
average_price = np.mean(df["Price"])

print("\n--- Average Product Price ---")
print(round(average_price, 2))


# 7. Category Wise Analysis
category_summary = df.groupby("Category").agg(
    Total_Products=("ProductID", "count"),
    Total_Stock=("Quantity", "sum"),
    Total_Value=("Price", lambda price: (price * df.loc[price.index, "Quantity"]).sum())
)

print("\n--- Category Wise Analysis ---")
print(category_summary)


# 8. Sort Products by Price
sorted_by_price = df.sort_values(by="Price", ascending=False)

print("\n--- Products Sorted by Price ---")
print(sorted_by_price.to_string(index=False))


# 9. Sort Products by Quantity
sorted_by_quantity = df.sort_values(by="Quantity", ascending=False)

print("\n--- Products Sorted by Quantity ---")
print(sorted_by_quantity.to_string(index=False))


# 10. Inventory Summary
inventory_summary = pd.DataFrame({
    "Metric": [
        "Total Products",
        "Total Available Stock",
        "Total Inventory Value",
        "Most Expensive Product",
        "Cheapest Product",
        "Average Product Price",
        "Low Stock Products"
    ],
    "Value": [
        total_products,
        total_stock,
        total_inventory_value,
        expensive_product["ProductName"],
        cheapest_product["ProductName"],
        round(average_price, 2),
        len(low_stock)
    ]
})

print("\n--- Final Inventory Summary ---")
print(inventory_summary.to_string(index=False))


# 11. Basic Data Validation
print("\n--- Data Validation ---")

print("Test 1:", "Passed" if df["ProductID"].is_unique else "Failed")
print("Test 2:", "Passed" if (df["Price"] >= 0).all() else "Failed")
print("Test 3:", "Passed" if (df["Quantity"] >= 0).all() else "Failed")
print("Test 4:", "Passed" if df.notnull().all().all() else "Failed")


# 12. Export Reports to CSV
os.makedirs("output", exist_ok=True)

inventory_summary.to_csv("output/inventory_summary.csv", index=False)
low_stock.to_csv("output/low_stock_products.csv", index=False)
category_summary.to_csv("output/category_summary.csv")

print("\nReports exported successfully!")
print("Check the output folder for CSV files.")
