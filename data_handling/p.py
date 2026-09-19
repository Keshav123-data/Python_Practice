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


# advance 

# Q. Given a list of employee salaries, find the employees earning above the average salary.

empl = {
    "keshav" : 20000,
    "mahesh" : 50000,
    "karan"  : 70000,
    "nagesh" : 10000,
    "om"     : 90000
}

avg = sum(empl.values()) / len(empl)

print("\naverage of total sales :",avg)

for name, salary in empl.items():
    if salary > avg:
        print("emplyees en=arns more than avg :",name, salary)

# using pandas
import pandas as pd

df6 = pd.DataFrame(list(empl.items()),columns = ("employee", "salary"))
print("\n",df6)

avg1 = df6[df6["salary"] > df6["salary"].mean()]

print("\nemployees enrning more than average:")
print(avg1)

# Q. From a list of numbers, find the top 3 highest values without using sort().
numbers = [23,45,78,3,45,78,89,4,23,5,57,8,90]

top_3 = []

for i in range(3):
    highest = max(numbers)
    top_3.append(highest)
    numbers.remove(highest)
    
print("top 3 highest numbers:",top_3)   

# Q. Given a list of names, find names that contain the letter "a".
names = ["keshav", "mahesh", "kirti", "om","rau"]

for i in names:
    if "a" in i.lower():
        print("names which contaiins 'a' :",i)

# Q. Count how many times each word appears in a sentence.

sentence = "welcome to python in the world of artificial intelligence"

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1

    else:
        word_count[word] = 1

print("\nword counts in sentence :", word_count)        

# Q. given 
sales1 = [1200, 1500, 900, 2200, 1800, 2500]

# Q1. total sales

total_sale = sum(sales1)
print("\ntotal sales:",total_sale)

# Q2. average sales

avg_sales = sum(sales1) / len(sales1)
print("\naverage sales:",avg_sales)

# Q3 highest sales

highest_sale = max(sales1)
print("\nhighest sales:",highest_sale)

# Q4 lowest sale

lowest_sale = min(sales1)
print("\nlowest sales:",lowest_sale)

# Q. Find the percentage increase from one month's sales to the next month.

previous_month = 1200
next_month = 1500

increase = ((next_month - previous_month) / previous_month) * 100
print("increase percentege : ",increase,"%")

for i in range(1, len(sales1)):
    increase1 = ((sales1[i]-sales1[i-1])/sales1[i-1]) * 100
    print("month:", 1, "increase percentage:",increase1,"%")

# Q. Given employee ages, divide employees into: Below 25 → Young, 25–40 → Adult, Above 40 → Senior

employee_ages = [18,16,50,70,30,50,70,20,38,15,18,30,16]

for i in employee_ages:
    if i < 25:
        print("young")

    elif i < 40:
        print("adult")

    else:
        print("senior")

# Q. Given a list of transaction amounts, separate positive and negative transactions.

transactions = [20000,-300,500,-900,45,-54,-56,34,-67,-67,34,876,]

pos_tra = []
neg_tra = []

for i in transactions:
    if i > 0:
        pos_tra.append(i)
    else:
        neg_tra.append(i)  
print("\npositive transactions:", pos_tra)
print("negative transactions:", neg_tra)   

# Q. Find all numbers that occur more than once in a list.

number = [10,10,20,30,50,60,30,40,20,30,90,60,80,70]

count_num = {}

for num in number:
    if num in count_num:
        count_num[num] += 1 
    else:
        count_num[num] = 1 
print("\nfrquency of numbers:", count_num)

duplicates = []

for num, frequency in count_num.items():
    if frequency > 1:
        duplicates.append(num)

print("numbers which are occurs frequency more than one:", duplicates)       

# Q. Create a dictionary containing each employee's name and salary, then find the employee with the highest salary.

dictionary = {
    "name" : ["keshav","mahesh","nagesh","karan","om","hari"],
    "salary" : [30000,40000,10000,60000,80000,30000]
}

print(dictionary)

max_salary = max(dictionary["salary"])
name = dictionary["name"][dictionary["salary"].index(max_salary)]

print("name of employee:", name)
print("highest salary", max_salary)
