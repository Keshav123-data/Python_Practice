import pandas as pd

data = {
    "Name": [" Amit ", "Priya", "Rahul", "Sneha ", "Amit"],
    "Age": [25, 28, None, 30, 25],
    "Salary": [45000, None, 40000, 65000, 45000],
    "Department": ["IT", "HR", "IT", None, "IT"]
}

df = pd.DataFrame(data)

print(df)
print(df.duplicated())