# Q.2 Write a program to check whether a number is positive, negative, or zero.
num = -1
if num > 0 :
    print ("Positive Number");
elif num == 0 :
    print ("Zero");
else:
    print ("Negative Number");


# Q. Check whether a person is eligible to vote.

age = 19 
if age >= 18:
    print("\nperson is eligible to vote")

# Q. Check whether a number is divisible by 5.

num = 25 
if num % 5 == 0:
    print("\nnumber is divisible by 5")

# Q. Find the largest of three numbers.

a = 29
b = 45 
c = 56
if a > b & c:
    print("\na is largest number")
elif b < a & c:
    print("\nb is largest number")
else:
    print("\nc is largest number")    

# Q. Check whether a year is a leap year.

year = 2028
if year % 4 == 0:
    print("\nyear is leap year")

# Q. Create a grading system:

mark = 87
if mark < 40:
    print("\nfail")
elif mark < 60:
    print("\nD Grade")
elif mark < 80:
    print("\nC Grade")
elif mark < 90:
    print("\nB Grade")
else:
    print("\nA Grade")

# Q. Check whether a number is divisible by both 3 and 5.

number = 46 
if number % 3 & 5 == 0:
    print("\n the number is divisible by both 3 and 5")

# Q. Create a simple calculator using if-elif.

A = 20
B = 5
operator = "/"

if operator == "+":
    print("\nresult:", A + B)
elif operator == "-":
    print("\nresult:", A - B)
elif operator == "*":
    print("\nresult:", A * B)
elif operator == "/":
    if B != 0:
        print("\nresult:",A / B)
    else:
        print("\ncan't devisible by 0")
else:
    print("\ninvalid operator")

# Q. Check whether a person is eligible for a loan based on age and salary.

Age = 21
Salary = 60000

if Age >= 18 & Age >=40000:
    print("\nperson is eligible for the loan")

# Q. Calculate electricity bill based on units consumed.

units = 15
bill = units * 10
print("\nelictricity bill:", bill)

# Q. Check whether a character is a vowel or consonant.

char = "Z"
if char == "aeiouAEIOU":
    print("\ncharacter is vowel")
else:
    print("\ncharacter is constant")

# Q. Check whether three sides can form a triangle.

s1 = 20
s2 = 50
s3 = 30

if s1+s2 > s3 & s1+s3 > s2 & s2+s3 > s1:
    print("\nthese three sides can from triangle")
else:
    print("\nthese three sides can not from triangle")

# Q. Categorize salary as Low, Medium, or High.

salary = 40000
if salary > 70000:
    print("\nSalary is High")
elif salary > 40000:
    print("\nSalary is medium")
else:
    print("\nSalary is low")

# Q. Create a login system using username and password.

real_username = "ADMIN"
real_password = 1234

username = input("\nEnter username:")
password = int(input("\nEnter the Password:"))

if username == real_username and password == real_password:
    print("\nLogin successfully")
else:
    print("\ninvalid username or password")

# Q. Check whether a number is a single-, double-, or triple-digit number.

numb = 233

if -10 > numb < 10:
    print("\ngiven number is single-digit number")
elif -100 > numb < 100:
    print("\ngiven number is double-digit number")
elif -1000 > numb < 1000:
    print("\ngiven number is three-digit number")
else:
    print("\ngiven number is mmore than three-digit number")

# Q. Create a discount calculator based on purchase amount.

amount = int(input("\nEnter the actual amount:"))

if amount >= 10000:
    discount = amount * 20 /100
elif amount >= 5000:
    discount = amount * 10 / 100
elif amount >= 2000:
    disount = amount * 5 / 100
else:
    discount = 0

final_amount = amount - discount
print("\npurchase_amount:",amount)
print("\ndisount:",discount)
print("\nfinal_amount:",final_amount)
