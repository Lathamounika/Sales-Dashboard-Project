import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('sales_data.csv')

# Convert OrderDate to datetime
data['OrderDate'] = pd.to_datetime(data['OrderDate'])

# Fill missing values if any
data.fillna(0, inplace=True)

# Add Month column
data['Month'] = data['OrderDate'].dt.month

# 1. Monthly Sales Analysis
monthly_sales = data.groupby('Month')['Quantity'].sum()
plt.figure(figsize=(8,5))
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Quantity Sold')
plt.grid(True)
plt.show()

# 2. Top Products
top_products = data.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
top_products.plot(kind='bar', title='Top 5 Products')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.show()

# 3. Sales by Region
region_sales = data.groupby('Region')['Quantity'].sum()
plt.figure(figsize=(6,6))
region_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Region')
plt.ylabel('')
plt.show()

# Optional: Category-wise Sales
category_sales = data.groupby('Category')['Quantity'].sum()
plt.figure(figsize=(6,6))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Quantity Sold')
plt.show()
