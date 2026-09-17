import pandas as pd 

df = pd.DataFrame({
    "order_ID" : [101,102,103,104,105,106],
    "product" : ["laptop","mouse","laptop","keyboard","mouse","laptop"],
    "resion" : ["south","north","north","south","east","east"],
    "sales" : [50000, 1500, 55000, 3000, 1800, 52000],
    "quantity" : [2,5,2,3,6,1]
})

print("DataFrame :")
print(df)

# Q. What is the total sales?

total_sales = df["sales"].sum()
print("\nTotal sales:", total_sales)

# Q. What is the average sales per order?

avg_sales_by_order = df["sales"].mean()
print("\naverage sales per order:")
print(avg_sales_by_order) 

# Q. Which product generated the highest sales?

highest_sale_product = (df.groupby("product")["sales"].sum()).sort_values(ascending=False).head(1)
print("\nhighest sales by products:",highest_sale_product)

# Q. Which region generated the highest sales?

highest_sales_resion = (df.groupby("resion")["sales"].sum()).sort_values(ascending=False).head(1)
print("\nhighest sales by resion:",highest_sales_resion)

# Q. What is the total quantity sold for each product?

total_quantity_by_products = df.groupby("product")["quantity"].sum()
print("\ntotal quantity by products:",total_quantity_by_products)

# Q. Find the average sales for each region.

avg_sales_by_resion = df.groupby("resion")["sales"].mean()
print("\naverage sales by resion:",avg_sales_by_resion)

# Q. Find the highest-value order.

highest_order = df.loc[df["sales"].idxmax()]
print("\nhighest order:",highest_order)

# Q. Add a column Sales_per_Unit.

df["sales_per_unit"] = df["sales"]/df["quantity"]
print("\nnew dataframe:",df)

# Q. Find products with total sales greater than ₹50,000.

total_sales_products = df.groupby("product")["sales"].sum()
greater_sales_products = total_sales_products[total_sales_products > 50000]
print("\nproducts which have sales greater than 50000:",greater_sales_products)

# Q. Create a summary DataFrame containing Product, Total Sales, Total Quantity, and Average Sales.

summary = df.groupby("product").agg(
    total_sales = ("sales","sum"),
    total_quantity = ("quantity","sum"),
    average_sales = ("sales","sum")
)

print("\nsummary:", summary)
