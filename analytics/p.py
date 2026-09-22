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

# Advance 
# Q. Combine two DataFrames using merge().

costomers = pd.DataFrame({
    "costomer_ID" :[101,102,103,104,105,106],
    "name" : ["keshav",'mahesh',"ganesh","karan","nagesh","om"],
    "city" : ["latur","pune","mumbai","nagpur","satara","ratnagiri"]
})

orders = pd.DataFrame({
    "order_id" : [1,2,3,4,5,6],
    "costomer_ID" : [101,103,104,103,102,102],
    "amount" : [134,256,564,864,345,3545]
})

Merged_df = pd.merge(costomers, orders, on = "costomer_ID")
print("\nMerged DataFrame:\n",Merged_df)

# Q. Practice left join, right join, and inner join.

innerjoin_df = pd.merge(
    costomers,
    orders,
    on = "costomer_ID",
    how = "inner"
)

print("\nInner joined DataFrame:\n", innerjoin_df)

leftjoined_df = pd.merge(
    costomers,
    orders,
    on = "costomer_ID",
    how = "left"
)

print("\nLeft Joined DataFrame:\n", leftjoined_df)

rightjoined_df = pd.merge(
    costomers,
    orders,
    on = "costomer_ID",
    how = "right"
)

print("\nRight Joined DataaFrame:\n",rightjoined_df)

# Q. Find customers who have not placed any orders.


left_join_df = pd.merge(
    costomers,
    orders,
    on = "costomer_ID",
    how = "left"
)

print("\nCostomers who are not placed any order:\n",left_join_df.loc[left_join_df["order_id"].isna(), "name"])

# Q. Find customers who placed more than 1 orders.

order_count = innerjoin_df.groupby("costomer_ID")["order_id"].count()
print("\nCostomers who are placed order more than one:\n",order_count[order_count > 1])

# Q. Calculate total revenue per customer.

print("\nTotal revenue per costomer:\n",left_join_df.groupby("name")["amount"].sum())

# Q. Calculate monthly sales using a date column.

data = {
    "Date": ["2026-01-05", "2026-01-15", "2026-02-10",
             "2026-02-20", "2026-03-05", "2026-03-15"],
    "Sales": [10000, 15000, 20000, 12000, 18000, 22000]
}

sales = pd.DataFrame(data)

print("\nSales DataFrame:\n",sales)

sales["Date"] = pd.to_datetime(sales["Date"])

monthly_sales = sales.groupby(
    sales["Date"].dt.to_period("M")
)["Sales"].sum()

print("\nMonthly Sales:\n", monthly_sales)

# Q. Find the best-selling product for each month.

data = {
    "Date": ["2026-01-05", "2026-01-15", "2026-01-20",
             "2026-02-10", "2026-02-15", "2026-02-20",
             "2026-03-05", "2026-03-15", "2026-03-20"],

    "Product": ["Laptop", "Mouse", "Laptop",
                "Keyboard", "Laptop", "Mouse",
                "Laptop", "Monitor", "Laptop"],

    "Sales": [50000, 5000, 45000,
              10000, 60000, 8000,
              55000, 30000, 65000]
}

df1 = pd.DataFrame(data)
print("\nDataFrame:\n", df1)

df1["Date"] = pd.to_datetime(df1["Date"])
df1["Month"] = df1["Date"].dt.to_period("M")

monthly_product_sales = df1.groupby(["Month","Product"])["Sales"].sum().reset_index()
print("\nSales by Month\n", monthly_product_sales)

print("\nbest Selling Products by Month:\n", monthly_product_sales.loc[monthly_product_sales.groupby("Month")["Sales"].idxmax()])

# Q. Find the highest-sales month.

sales_pr_month = df1.groupby("Month")["Sales"].sum()
print("\nHighest Sales Month:", sales_pr_month.idxmax())
print("\nHighest Sales:",sales_pr_month.max())

# Q. Calculate month-over-month sales growth.

print("\nmonth-over-month sales growth:\n",monthly_sales.pct_change() * 100)

# Q. Create a pivot table showing: Region × Product → Total Sales

pivot_table = pd.pivot_table(
    DataFrame,
    index = "Region",
    columns = "Product",
    values = "Sales",
    aggfunc = "sum",
    fill_value = 0
)

print("\nPivot Table:\n", pivot_table)

# Q. Create a pivot table showing: Department × Gender → Average Salary

company = pd.DataFrame(
    {
        "Name" : ["keshav","kriti","nagesh","karina","nikita"],
        "Department" : ["IT","Finanace","HR","IT","HR"],
        "Gender" : ["Male", "Female","Male","Female","Female"],
        "Salary" : [60000,40000,80000,30000,70000]
    }
)

print("\nDataFrame:\n", company)

pivot = pd.pivot_table(
    company,
    index = "Department",
    columns = "Gender",
    values = "Salary",
    aggfunc = "mean",
    fill_value = 0
)

print("\nCompany Pivot Table:\n",pivot)

# Q. Use groupby() with multiple columns.

print("\nDataFrame:\n",company.groupby(["Department","Gender"])["Salary"].sum())

# Q. Use agg() to calculate: sum, mean, minimum, maximum.

print("\nAgg() functions on sales:\n",company["Salary"].agg(["sum","mean","min","max"]))

# Q. Find duplicate customer IDs.

print("\nDataFrame", innerjoin_df)

print("\nDuplicate Costomer IDs:\n", innerjoin_df[innerjoin_df.duplicated()])

# Q. Identify customers whose total purchase is above the average customer purchase.

total_amount = innerjoin_df.groupby("costomer_ID")["amount"].sum()

avg_amount = innerjoin_df["amount"].mean()

print("\nCostomers who pusrched more than the average amount:\n",total_amount[total_amount > avg_amount])