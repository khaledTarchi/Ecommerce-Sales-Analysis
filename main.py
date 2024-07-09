#______ E-Commerce Sales Analysis Project________


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("ecommerce_sales_analysis.csv")


print("Basic Information")
print(df.info())
print("\n")

print("First 5 Rows")
print(df.head())
print("\n")

print("Descriptive Statistics")
print(df.describe())
print("\n")


print("Missing Values")
print(df.isnull().sum())
print("\n")


df.fillna(0, inplace=True)

df['product_id'] = df['product_id'].astype(str)
df['product_name'] = df['product_name'].astype(str)
df['category'] = df['category'].astype(str)


df['total_sales'] = df[['sales_month_1', 'sales_month_2', 'sales_month_3', 'sales_month_4', 'sales_month_5',
                        'sales_month_6', 'sales_month_7', 'sales_month_8', 'sales_month_9', 'sales_month_10',
                        'sales_month_11', 'sales_month_12']].sum(axis=1)


top_categories = df.groupby('category')['total_sales'].sum().sort_values(ascending=False)
print("Top-Performing Product Categories")
print(top_categories)
print("\n")




plt.figure(figsize=(10, 6))
sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
plt.title('Top-Performing Product Categories')
plt.xlabel('Total Sales')
plt.ylabel('Category')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='price', y='total_sales', data=df, hue='category', palette='viridis')
plt.title('Price vs Total Sales')
plt.xlabel('Price')
plt.ylabel('Total Sales')
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='price', y='review_score', data=df, hue='category', palette='viridis')
plt.title('Price vs Review Score')
plt.xlabel('Price')
plt.ylabel('Review Score')
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.show()


monthly_sales = df.groupby('category')[['sales_month_1', 'sales_month_2', 'sales_month_3', 'sales_month_4', 
                                        'sales_month_5', 'sales_month_6', 'sales_month_7', 'sales_month_8', 
                                        'sales_month_9', 'sales_month_10', 'sales_month_11', 'sales_month_12']].sum().T

monthly_sales.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

plt.figure(figsize=(12, 8))
monthly_sales.plot()
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend(title='Category')
plt.grid(True)
plt.show()


avg_review_score = df.groupby('category')['review_score'].mean().sort_values(ascending=False)
print("Average Review Score by Category")
print(avg_review_score)
print("\n")


plt.figure(figsize=(10, 6))
sns.barplot(x=avg_review_score.values, y=avg_review_score.index, palette='viridis')
plt.title('Average Review Score by Category')
plt.xlabel('Average Review Score')
plt.ylabel('Category')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='review_count', y='review_score', data=df, hue='category', palette='viridis')
plt.title('Review Count vs Review Score')
plt.xlabel('Review Count')
plt.ylabel('Review Score')
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.show()


df.to_csv('cleaned_ecommerce_sales.csv', index=False)

print("E-Commerce Sales Analysis Completed Successfully.")