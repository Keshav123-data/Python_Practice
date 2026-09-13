# Q Given a list of salaries, find the minimum, maximum, average, and median.
salary = [10000,20000,24000,45000,20000,40000,60000]
print("salaries:",salary)

min_salary = min(salary)
max_salary = max(salary)
avg_salary = sum(salary)/len(salary)
salary.sort()
n = len(salary)

if n % 2 == 1:
    mid_salary = salary[n//2]
else:
    mid_salary = salary[n // 2 - 1] + salary[n // 2] / 2

print("minimum salary:",min_salary)
print("max salary :", max_salary)
print("average salary:",avg_salary)
print("median salary:",mid_salary)


# Q Given a list containing None values, remove all missing values.
list1 = [1,None,2,3,None,4,5,None,6,None,7,None,8,None,9,None,10]
new_list = []
for i in list1:
    if i is not None:
        new_list.append(i)
print(new_list)        


# Q Convert a list of strings like ["100", "250", "300"] into integers.
str_list = ["100","250","300"]
int_list = []
for i in str_list:
    int_list.append(int(i))

print(int_list)

# Q. Given sales data, calculate the total sales for each product.

sales = {
    ("Laptop", 50000),
    ("Mobile",15000),
    ("Laptop",45000),
    ("Mobile",20000),
    ("Laptop",60000)
}

Total_sales = {}

for product, prize in sales:
    if product in Total_sales:
        Total_sales[product] += prize  # same for frequncy count just change prize to 1 in conditions 
    else:
        Total_sales[product] = prize

print(Total_sales)

# Q. Find all employees whose salary is greater than ₹50,000.

salary1 = {
    ("keshav",80000),
    ("mahesh", 40000),
    ("karan",90000),
    ("nagesh",100000),
    ("mohan",55000),
    ("nitin",33000)
}
max_salary_emp = []
for i, m in salary1:
    if m > 50000:
        max_salary_emp.append(i)
print(max_salary_emp)   

# Q. Sort a list of dictionaries based on salary.

employees = [
    {"name":"keshav","salary":60000},
    {"name":"nagesh","salary":70000},
    {"name":"karan","salary":80000},
    {"name":"mahesh","salary":40000}
]

employees.sort(key=lambda x: x["salary"], reverse=False)

print(employees)


# Q. Count the number of employees in each department.
company = {
    ("IT","keshav"),
    ("Sales", "mahesh"),
    ("IT","rahul"),
    ("Marketing","nagesh"),
    ("HR","kriti"),
    ("Sales","karan"),
    ("Marketing","nikita"),
    ("IT","rohini")
}

e_count = {}
for dep,emp in company:
    if dep in e_count:
        e_count[dep] += 1
    else:
        e_count[dep] = 1

print(e_count)   

# Q. Find the employee with the highest salary in each department.

emps = [
    {"name": "Rahul", "department": "IT", "salary": 50000},
    {"name": "Amit", "department": "HR", "salary": 40000},
    {"name": "Sneha", "department": "IT", "salary": 70000},
    {"name": "Priya", "department": "HR", "salary": 55000},
    {"name": "Rohit", "department": "Sales", "salary": 45000},
    {"name": "Neha", "department": "Sales", "salary": 60000}
]


highest_earner = {}

for emp in emps:
    dep = emp["department"]

    if dep not in  highest_earner:
        highest_earner[dep]= emp

    elif emp["salary"] > highest_earner[dep]["salary"]:
        highest_earner[dep] = emp

print("Highest earner by department:",highest_earner)

# Q. Given daily sales, calculate the day with the highest sales.
sales_days =  {
    "Monday": 12000,
    "Tuesday": 18000,
    "Wednesday": 15000,
    "Thursday": 22000,
    "Friday": 17000
}

highest_day = ""
highest_sales = 0
for day, sales in sales_days.items():
    if sales > highest_sales:
        highest_sales = sales
        highest_day = day

print("Highest sales day is", highest_day, "with sales of ₹", highest_sales)


# Q. Calculate the percentage contribution of each product to total sales.

sales_product = [
    ("Laptop", 50000),
    ("Mobile", 15000),
    ("Tablet", 30000),
    ("Laptop", 45000),
    ("Mobile", 20000),
    ("Tablet", 25000)
]

total_sales_pr = {}

for pr,sal in sales_product:
    if pr in total_sales_pr:
        total_sales_pr[pr] += sal
    else:
        total_sales_pr[pr] = sal

print(total_sales_pr)

grand_total = sum(total_sales_pr.values())

print(grand_total)


for pr,sal in total_sales_pr.items():
    percentage = (sal / grand_total) * 100
    print(pr,":",round(percentage,2),"%")


