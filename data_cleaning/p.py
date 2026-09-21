import pandas as pd

data = {
    "Name": [" Amit ", "Priya", "Rahul", "Sneha ", " Amit "],
    "Age": [25, 28, None, 30, 25],
    "Salary": [45000, None, 40000, 65000, 45000],
    "Department": ["IT", "HR", "IT", None, "IT"]
}

df = pd.DataFrame(data)

print("DataFrame:\n",df)

# Q. Find all missing values.

print("\nnull vlaues:\n",df.isnull())

# Q. Count missing values in each column.

print("\nnumber of mising values in each columns:\n", df.isnull().sum())

# Q. Calculate the percentage of missing values in each column.

print("\npercentage of missing values in each column:\n", df.isnull().mean() * 100)

# Q. Fill missing Age with the average age.

avg_age = df["Age"].mean()
df["Age"]= df["Age"].fillna(avg_age, inplace=True)
print("\n",df)

# Q. Fill missing Salary with the median salary.

df["Salary"] = df["Salary"].fillna(df["Salary"].median(),inplace=True)
print("\n",df)

# Q. Fill missing Department with "Unknown".

df["Department"] = df["Department"].fillna("Unknown", inplace = True)
print("\n",df)

# Q. Remove rows containing missing values.

df = df.dropna()
print("\n",df)

# Q. Remove duplicate rows.
print("\nduplicate values:\n",df.duplicated()) 
df = df.drop_duplicates()
print("\nDataFrame:",df)

# Q. Remove extra spaces from the Name column using .str.strip().

df["Name"] = df["Name"].str.strip()

print("\n",df)

# Q. Convert names to uppercase.

df["Name"] = df["Name"].str.upper()
print("\n",df)

# Q. Convert names to lowercase.

df["Name"] = df["Name"].str.lower()
print("\n",df)

# Q. Check the data types of all columns.

print("\ndata types:\n", df.dtypes)

# Q. Convert the Age column to integer after handling missing values.

df["Age"] = df["Age"].astype(int)
print("\n",df.dtypes)

# Q. Rename Salary to Monthly_Salary.
df.rename(columns = {"Salary":"Monthly_Salary"}, inplace=True)
print("\n",df)

# Q. Create a Yearly_Salary column.

df["Yearly_Salary"] = df["Monthly_Salary"] * 12 

print("\n", df)
