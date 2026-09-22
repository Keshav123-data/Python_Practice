# Q. Create a DataFrame from a dictionary containing employee data.
import pandas as pd
employee_data = {
    "name" : ["keshav","mahesh","nagesh","mahesh"],
    "salary" : [70000,50000,60000,50000],
    "age" : [23,45,23,45]
}

df = pd.DataFrame(employee_data)
print(df)
print(type(df))

# Q. Select employees whose salary is greater than ₹60,000.

result = df[df["salary"] >= 60000]
print(result)

# Q. Find and remove duplicate rows.
duplicates = df[df.duplicated()]
print("duplicated columns:")
print(duplicates)

df =  df.drop_duplicates()
print(df)

# Q. Detect missing values in every column.

students = {
    "name":["keshav", "mahesh",None,"karan"],
    "age":[23,None,34,35],
    "location":["pune","mumbai","delhi",None]
}

df1 = pd.DataFrame(students)
print(df1)

print( df1.isnull())
print(df1.isnull().sum())

# Q. Fill missing salary values with the average salary.
average_mean =df1["age"].mean()
print(average_mean)

df1["age"] = df1["age"].fillna(average_mean, inplace = True)
print(df1)

# Q. Group employees by department and calculate average salary.

emp = {
    "name" : ["keshav","mahesh","nagesh","karan"],
    "age" : [23,24,24,25],
    "department" : ["IT", "HR","IT","Finance"],
    "salary": [80000,60000,30000,50000]
}

df2 = pd.DataFrame(emp)
print(df2)

result1 = df2.groupby("department")["salary"].mean()

print("department wise averaged salary")
print(result1)


# Q. Find the top 5 highest-paid employees.

employees = {
    "name":["keshav","mahesh","nagesh","karan","hari","om","rahul","kirti","abhi"],
    "salary":[30000,50000,60000,10000,30000,50000,80000,90000,10000]
}

df3 = pd.DataFrame(employees)
print(df3)

sorted_df = df3.sort_values("salary", ascending=False)
print(sorted_df.head())


# Q. Sort a DataFrame by salary in descending order.

sorted_df1 = df3.sort_values("salary", ascending=False)
print(sorted_df1)

# Q. Add a new column called Annual_Salary.

df3["annual_salary"] = df3["salary"] * 12

print("new DataFrame:")
print(df3)


# Q. Rename multiple columns at once.
df3 = df3.rename(columns = {
    "name":"emp_name",
    "salary":"emp_salary"
})

print(df3)

# Q. Filter rows using multiple conditions.
dataframe = {
    "name":["keshav","mahesh","nagesh","karan","nagesh","om"],
    "department":["IT","Finance","IT","HR","IT","Finance"],
    "salary":[30000,50000,60000,20000,70000,60000]
}

df4 = pd.DataFrame(dataframe)
print(df4)

Conditional_df =df4[(df4["department"] =="IT") & (df4["salary"] >=50000)]

print(Conditional_df)

# Q. Use value_counts() to find the most common job role.

df4["job"] = ["analyst", "data_eng","sql_administrator", "analyst", "accountant","analyst"]
print(df4)

job_counts = df4["job"].value_counts()
print(job_counts)

common_role = job_counts.sort_values(ascending=False).head(1)
print("common role:",common_role)

# Q. Use groupby() to calculate total sales by region.

sales_df = {
    "product":["phone","headphone","laptop","pen","TV","shirt"],
    "region":["south","north","west","east","east","south"],
    "sales":[150,350,607,207,450,943]
}

df5 = pd.DataFrame(sales_df)
print(df5)

ts_by_re = df5.groupby("region")["sales"].sum()
print("total sales by the region :", ts_by_re)


# Q. Use merge() to combine customer and order DataFrames.

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

res = pd.merge(costomers ,orders , on = "costomer_ID")
print("merged_Dataframe:", res)

# Q. Create a pivot table showing sales by region and product.

pivot = pd.pivot_table(
    df5,
    index = "region",
    values = "sales",
    columns = "product",
    aggfunc = "sum"
    )

print(pivot)

# Q. create thsis DataFrame 

import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Amit"],
    "Age": [25, 28, 24, 30, 25],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [45000, 55000, 40000, 65000, 45000]
}

new_df = pd.DataFrame(data)

print("\nDataFrame:\n",new_df)

# Q. Display the first 3 rows.

print("\ntop three rows:\n",new_df.head(3))

# Q. Display the last 2 rows.

print("\nbottom 3 rows:\n",new_df.tail(3))

# Q. Find the number of rows and columns.

rows, columns = new_df.shape
print("\nnumber of rows:", rows)
print("number of columns:", columns)

# Q. Display only the Name and Salary columns.

print("\n",new_df[["Name","Salary"]])

# Q. Find employees whose salary is greater than ₹50,000.

print("\nemployees whose salary is greter than 50000:\n",new_df[new_df["Salary"]> 50000])

# Q. Find employees whose age is greater than 25.

print("\nemployees whose age is greater than 25:\n", new_df[new_df["Age"] > 25])

# Q. Find employees working in the IT department.

print("\nemployees whose are from IT department:\n", new_df[new_df["Department"] == "IT"])

# Q. Find the average salary.

print("\naverage dalary:\n", new_df["Salary"].mean())

# Q. Find the maximum salary.

print("\nmaximum salary:\n",new_df["Salary"].max())

# Q. Find the employee with the minimum salary.

print("\nemployee whose salary is minimun:\n", new_df.loc[new_df["Salary"].idxmin()])

# Q. Find the number of employees in each department.

print("\nnumber of employees in each department:\n", new_df["Department"].value_counts())

# Q. Calculate the average salary for each department.

print("\naverage salary by each department:\n", new_df.groupby("Department")["Salary"].mean())

# Q. Sort employees by salary from highest to lowest.

print("\nsorted salary descending:\n",new_df.sort_values(by = "Salary", ascending = False))

# Q. Add a column called Annual_Salary.

new_df["Annual_Salary"] = new_df["Salary"] * 12 
print("\n",new_df)

# Q. Remove duplicate employees.
new_df = new_df.drop_duplicates()
print("\n",new_df)

# Q. Find employees whose salary is above the average salary.

above_average = new_df.loc[new_df["Salary"] > new_df["Salary"].mean(), "Name"]
print("\nemployees whose salary is greater than avrerage of salary:\n",above_average)

# Q. Find the average age of employees in each department.

a = new_df.groupby("Department")["Age"].mean()
print("\naverage age of each department:\n",a)

# Q. Find the highest salary in each department.

print("\nhighest salary by Department:\n:",new_df.groupby("Department")["Salary"].max())

# Q. Find the lowest salary in each department.
print("\nlowest salary in each department:\n", new_df.groupby("Department")["Salary"].min())

# Q. Find the employee with the highest salary in each department.
print("\nemployees whose Salary is highest in each Department:\n",new_df.loc[new_df.groupby("Department")["Salary"].idxmax()])

# Q. Count how many employees are in each department.
print("\nnumber of employees in each department:\n",new_df["Department"].value_counts())

# Q. Find the percentage of employees belonging to each department.

print(new_df["Department"].value_counts(normalize=True) * 100)

# Q. Create a new column: "Salary_Category" Salary < 45,000 → Low,45,000 - 60,000 → Medium, 60,000 → High

new_df["Salary_Category"] = pd.cut(
    new_df["Salary"],
    bins= [0, 45000, 60000, float("inf")], # inf = infinity
    labels = ["low","medium","high"]
)
print("\n", new_df)

# Q. Find how many employees belong to each salary category.

print("\n", new_df["Salary_Category"].value_counts())

# Q. Find employees whose salary is between ₹40,000 and ₹60,000.

print("\n", new_df.loc[(new_df["Salary"] >= 40000) & (new_df["Salary"] <= 60000)])