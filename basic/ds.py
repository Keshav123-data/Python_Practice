# Q. Remove duplicate values from a list.
list1 = [1,2,3,2,3,4,2,3,1,2,4,2,3,1,4]
list1 = list(set(list1))
print(list1)


list2 = ["a","b","c","a","c","b","b","a","c"]
list2 = list(set(list2))
print(list2)

# Q. Find the second-largest number in a list.
list_n = [10,230,3540545,505050,453993,94,95405495]
list_n.sort()
second_largest = list_n[-2]
print ("second largest number is :",second_largest )

# Q. Create a list of 10 numbers.

list3 = [1,4,3,7,9,8,10,2,5,6]
print("list:", list3)

# Q. Create a list of 10 numbers.

largest = max(list3)
print("largest number:", largest)

# Q. find the smallest number

smallest = min(list3)
print("smallest number:", smallest)

# Q. calculate the sum and average

sum1 = sum(list3)
avg = sum1 / len(list3)
print("total of umbers:", sum1)
print("average of numbers:",avg)

# Q. count even and odd numbers 

even_count = 0
odd_count = 0
for i in list3:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("even count", even_count)
print("odd count", odd_count)

# Q. Remove duplicate values.

num1 = [1,3,4,2,2,3,4,5,1,3,4,7,9,5,9,7,6,8,5,4,3]
unique = []

for i in num1:
    if i not in unique:
        unique.append(i)
print("unique list:", unique)

# Q. Find the second-largest number.

list3.sort()
print("second largest number is:",list3[-2])

# Q. Sort numbers in ascending order.

list3.sort()
print("list:",list3)

# Q. Sort numbers in descending order.

list3.sort(reverse=True)
print("list:", list3)

# Q. Find numbers greater than the average.

total = sum(num1)
average = total / len(num1)

for i in num1:
    if i > average:
        print(i)

# Q. Find all numbers greater than 50.

numbers = [10,50,30,60,38,70,90,80,60]

for i in numbers:
    if i > 50:
        print(i)

# Q. Find all negative numbers.

numb = [-14,6,4,-6,-8,-35,78,98,-56,89,76,-87,-27,]

for i in numb:
    if i < 0:
        print("negative numbers:", i)

# Q. Replace negative numbers with zero.

result = []
for i in numb:
    if i < 0:
        result.append(0)
    else:
        result.append(i)
print("list:",result)

# Q. Combine two lists.

x = [11,22,33,44,55]
y = [66,22,88,99,55]

combined = x + y
print("combined list:", combined)

# Q. Find common elements between two lists.

common = []
for i in x:
    if i in y:
        common.append(i)
print("common number:", common)

# Q. Find elements present in one list but not another.

unique_element = []
for i in x:
    if i not in y:
        unique_element.append(i)
print("unique elements from list to another:", unique_element)

# Q. Create a list of squares from 1 to 20.

square = []

for i in range(1,21):
    square.append(i * i)
print("square of numbers:", square)

# Q. Create a list containing only even numbers.

even_list = []

for i in range(1,21):
    if i % 2 == 0:
        even_list.append(i)
print("list containing only even numbers:", even_list)


# Q. Find duplicate values.

duplicate = []

for i in num1:
    if num1.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
print("duplicates:", duplicate)

# Q. Count the frequency of every value.

frequncy = {}

for i in num1:
    if i in frequncy:
        frequncy[i] += 1
    else:
        frequncy[i] = 1
print("frequncy", frequncy)

# Q. Create a tuple containing employee information.

tup = ("keshav",23,"Latur", 30000)
print("tuple",tup)

# Q. Access elements from a tuple.

print(tup[0])
print(tup[1])

# Q. Convert a tuple into a list.

new_list = list(tup)
print("list:", new_list)

# Q. Find unique values using a set.

z = (1,3,4,3,5,7,8,6,4,3,6,8,8,5,4,4,6,8,9,7,5,9)

unique_tup = set(z)
print("unique tupple:", unique_tup)

# Q. Find common values between two sets.

x_set = {1,2,3,4,5,6}
y_set = {4,5,6,7,8,9}

for i in x_set:
    if i in y_set:
        print(i)

print(x_set.intersection(y_set))

# Q. Find the union of two sets.

print(x_set.union(y_set))

# Q. Find the difference between two sets.

print(x_set.difference(y_set))

# Q. Create a dictionary containing employee names and salaries.
dict1 = {
    "keshav" : 50000,
    "mahesh" : 40000,
    "nagesh" : 30000
}
print("dict:", dict1)

# Q. Find the employee with the highest salary.

max_salary = max(dict1.values())
for name, salary in dict1.items():
    if salary == max_salary:
        print(name,salary)

# Q. Find the employee with the lowest salary.

low_salary = min(dict1.values())
for name, salary in dict1.items():
    if salary == low_salary:
        print(name, salary)

# Q. Add a new employee to the dictionary.

dict1["karan"] = 56000
print(dict1)

# Q. Update an employee's salary.

dict1["keshav"] = 60000
print(dict1)

# Q. Remove an employee.

del dict1["karan"]
print(dict1)

# Q. Count the frequency of words using a dictionary.

fruits = ["apple", "banana", "banana", "apple", "banana", "orange"]

count = {}

for i in fruits:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

# Q. Create a dictionary from two lists.

rate = [80,35,35,80,35,60]

dic = dict(zip(fruits,rate))
print(dic)

# Q. Sort a dictionary by values.
sort_by_value = dict(sorted(dic.items(), key = lambda x : x[1]))

print(sort_by_value)

# Q. Find employees earning more than ₹50,000.

for name, salary in dict1.items():
    if salary > 50000:
        print(name, salary)

# Q. Group employees according to department.

employees = {
    "Keshav": "IT",
    "Mahesh": "HR",
    "Karan": "IT",
    "Om": "Finance",
    "Nagesh": "HR",
    "Rahul": "IT"
}

departments = {}

for name, depart in employees.items():
    if depart not in departments:
        departments[depart] = []
    departments[depart].append(name)
print(departments)
    