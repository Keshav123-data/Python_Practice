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


data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse",
                "Monitor", "Keyboard", "Laptop"],
    "Region": ["North", "South", "East", "West", "North",
               "South", "East", "North"],
    "Sales": [55000, 1200, 2500, 60000, 1500, 18000, 3000, 58000],
    "Quantity": [2, 5, 3, 2, 6, 2, 4, 2]
}

DataFrame = pd.DataFrame(data)
print("\nDAtaFrame", DataFrame)

# Q. Calculate total sales.
print("\nTotal Sales:\n",DataFrame["Sales"].sum())

# Q. Calculate average sales.
print("\nAverage Sales:\n", DataFrame["Sales"].mean())

# Q. Find the highest sales transaction.
print("\nHighest Sales Transaction:\n",DataFrame["Sales"].max())

# Q. Find the lowest sales transaction.
print("\nLowest Sales Transaction:\n", DataFrame["Sales"].min())

# Q. Find total quantity sold.

print("\nTotal Quantity:\n",DataFrame["Quantity"].sum())

# Q. Find total sales by product.

print("\nTotal Sales by Products:\n", DataFrame.groupby("Product")["Sales"].sum())

# Q. Find total sales by region.

print("\nTotal Sales by Region:\n", DataFrame.groupby("Region")["Sales"].sum())

# Q. Find average sales by region.

print("\nAverage Sales by Region:\n", DataFrame.groupby("Region")["Sales"].mean())

# Q. Find the product with the highest total sales.
print("\nProduct with Highest Total Sales:\n",(DataFrame.groupby("Product")["Sales"].sum()).idxmax())

# Q. Find the region with the highest total sales.

print("\nRegion with highest Total Sales:\n", (DataFrame.groupby("Region")["Sales"].sum()).sort_values(ascending=False).head(1))

# Q. Find total quantity sold for each product.
print("\nTotal Quantity by Prouduct:\n", DataFrame.groupby("Product")["Quantity"].sum())

# Q. Add a column: Sales_Per_Unit = Sales / Quantity

DataFrame["Sales_Per_Unit"] = DataFrame["Sales"] / DataFrame["Quantity"]

print("\nNew DataFrame:\n", DataFrame)

# Q. Find the product with the highest sales per unit.

pr_max_per_unit = DataFrame.groupby("Product")["Sales_Per_Unit"].max()
print("\nProduct with Highest Sales Per Unit:\n", pr_max_per_unit )

# Q. Find the top 3 sales transactions.
print("\nTop 3 Sales Transactions:\n", DataFrame.sort_values("Sales", ascending=False).head(3))

# Q. Find all transactions where sales are greater than ₹20,000.

print("\nSales which are greater than 20000:\n", DataFrame[DataFrame["Sales"] > 20000])

