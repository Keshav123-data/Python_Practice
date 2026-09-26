# Q. Store your name, age, city, and salary in variables and print them.

name = "keshav"
age = 23 
city = "Latur"
Salary = 30000

print("\nmy information:\n", name, age, city, Salary)

# Q. Take two numbers from the user and calculate their sum.

num1 = int(input("Enter the number1 :"))
num2 = int(input("Enter thr number2 :"))
sum = num1 + num2
print("\nsum of two numbers:",sum)

# Q. Calculate the difference, multiplication, and division of two numbers.

a = 2
b = 6
dif = b - a
multi = a *  b
divi = b / a

print("\ndiffrence:",dif)
print("\nmiltiplication:",multi)
print("\ndivision:", divi)

# Q. Calculate the area of a rectangle.

length = 12
width = 15
area = length * width 
print("\narea of rectangle:", area)

# Q. Take a user's age and calculate their age after 10 years.

age =  int(input("\nEnter your Age:"))
after_10_years_age = age + 10
print("\nAfter 10 years age will be:",after_10_years_age)

# Q. Check whether a number is positive, negative, or zero.

number = int(input("\nenter your number:"))
if number > 0:
    print(number,":Number is positive")
elif number == 0:
    print(number,":number is zero")
else:
    print(number,":number is negative")

# Q. Check whether a number is even or odd.

numb = int(input("\n Enter your number:"))
if numb % 2 == 0:
    print("\ngiven number is even")
else:
    print("\ngiven number is odd")

# Q. Take marks of 5 subjects and calculate total and percentage.

sub1 = 89
sub2 = 90
sub3 = 78
sub4 = 98
sub5 = 87

total = sub1 + sub2 + sub3 + sub4 + sub5
print("\ntotal:",total)
print("\npercentage:",total / 5 )

# Q. Calculate simple interest.

p = 10000
r = 5
t = 2

simple_interest = (p * r * t) / 100

print("\nsimple interest:",simple_interest)

# Q. Convert minutes into hours and minutes.

minutes = 110
hours = minutes // 60
remaining_minutes = minutes % 60
print("\ntime in hours and minutes:",hours,":",remaining_minutes)

# Q. Swap two variables.

a1 = 10
b1 = 25

a1,b1 = b1,a1
print("\na1 = ", a1)
print("b1 = ", b1)

# Q. Compare two numbers and print the greater number.

x = 16
y = 67

if x > y:
    print("\nx is greter than y")
else:
    print("\ny is greter than x")

# Q. Calculate the average of three numbers.

A = 23
B = 45
C = 98

average_number = (A + B + C) / 3
print("\naverage number:",average_number)

# Q.1 Create variables for a person's name, age, and salary and print them.

name = "keshav"
age = 23
salary = 20000

print(name)
print(age)
print(salary)