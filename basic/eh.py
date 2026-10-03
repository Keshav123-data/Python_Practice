# Q. Handle division-by-zero errors.

try:
    num1 = 10
    num2 = 0 

    result = num1 / num2
    print(result)

except  ZeroDivisionError:
    print("can not divide by zero")

# Q. Handle invalid user input.

try:
    number = input(int("enter the number:"))
    print("you entered number:", number)

except ValueError:
    print("invalid input please enter the real number")

# Q. Create a calculator with exception handling.

try:
    number1 =  12 # float(input("enter the number:"))
    operator = "*" # input("enter operator (+, -, *, /):")
    number2 =  2 # float(input("enter the number:"))

    if operator == "+":
        result = number1 + number2

    elif operator == "-":
        result = number1 - number2

    elif operator == "*":
        result = number1 * number2

    elif operator == "/":
        result = number1 / number2

    else:
        print("operator is invalid")
        result = None

    if result is not None:
        print("reslut", result)

except ValueError:
    print("numbers are invalid")

except ZeroDivisionError:
    print("cannot devide by zero")

# Q. Read a text file and count the number of lines.

file = open("C:/Users/keshav shinde/OneDrive/Desktop/Python_Practice/basic/basic.py","r")
lines = file.readlines()
print("number of lines:",len(lines))
file.close()

with open("C:/Users/keshav shinde/OneDrive/Desktop/Python_Practice/basic/basic.py","r") as file:
    lines = file.readlines()
print("number of lines:", len(lines))

# Q. Count words in a text file.
with open("C:/Users/keshav shinde/OneDrive/Desktop/Python_Practice/basic/text.txt","r") as file1:
    text = file1.read()
    words = text.split()
print("number of words:", len(words))

# Q. Find the longest line in a file.

longest_line = max(lines, key = len)
print("longest line:", longest_line.strip())


# Write employee data to a text file.

employees = [
    ["keshav", 23, "IT", 50000],
    ["mahesh", 22, "finance", 40000],
    ["karan", 24, "HR", 60000]
]

with open("C:/Users/keshav shinde/OneDrive/Desktop/Python_Practice/basic/employees.txt","w") as file2:
    for employee in employees:
        file2.write(
            f"name : {employee[0]},"
            f"age : {employee[1]},"
            f"department : {employee[2]},"
            f"salary : {employee[3]}\n"
        )
print("employee data written successfully")

# Q. Read employee data from a file.

with open("C:/Users/keshav shinde/OneDrive/Desktop/Python_Practice/basic/employees.txt","r") as file3:
    e_data = file3.read()
print(e_data)

# Q. Read a CSV file using Python.

import csv
with open("C:/Users/keshav shinde/Downloads/industry.csv","r", encoding="utf-8") as csv_file:
    csv_data = csv.reader(csv_file)

    for row in csv_data:
        print(row)

# Q. Calculate total rows from a CSV file.
import csv

file_path = "C:/Users/keshav shinde/Downloads/industry.csv"

with open(file_path, "r", encoding="utf-8") as file4:
    reader = csv.reader(file4)

    next(reader)  # Skip header

    total_rows = 0

    for row in reader:
        total_rows += 1

print("Total rows:", total_rows)
