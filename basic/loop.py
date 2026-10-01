# Q. Count how many even numbers are present in a list.

list = [1,2,3,4,5,6,7,8,9]
count = 0
for n in list:
    if n % 2 == 0:
        count += 1
print("Count of even number in the list is:", count)

# Q. Count how many odd numbers are present in a list.
list = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in list:
    if i % 2 != 0:
        count +=1
print("Count of odd number in the list is:", count)

# find the even and odd numbers in a list and create a new list for even and odd numbers.
list2 = [1,2,3,4,5,6,7,8,9]
even_numbers = []
odd_numbers = []
for i in list2:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("Even Numbers", even_numbers)
print("Odd Numbers", odd_numbers)

# Q. Calculate the average of numbers in a list.
list = [1,2,5,3,6,8,5,4]
sum1 = 0
for i in list:
    sum1 += i
average = sum1 / len(list)
print(average)

list1 = [2,5,3,6,8,6,4,3,5,67,8,6,43,3,55,768,8,54,3,45]
average1 = sum(list1)/len(list1)
print(average1)

# Q. Count the frequency of each element in a list.
list1 = [1,2,3,1,3,4,6,4,3,1,3,4,4,5,4,3,2,3,4,5,4,3,2]
frequency = {}
for i in list1:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)

# Q. Reverse a string without using [::-1].
text = "hello"
reversed_text = ""  
for char in text: # Iterate through each character in the string
    reversed_text = char + reversed_text   # added the new character to the before of the reversed string
print(reversed_text)


# Q. Print numbers from 1 to 100.

print("\nNumbers:")
for i in range(1,101):
    print(i)

# Q. Print all even numbers from 1 to 100.

print("\nEven number:")
for i in range(1,101):
    if i % 2 == 0:
        print(i)

# Q. Print all odd numbers from 1 to 100.

print("\nOdd Numbers:")
for i in range(1,101):
    if i % 2 != 0:
        print(i)

# Q. Find the sum of numbers from 1 to 100.
total = 0
for i in range(1,101):
    total = total + i
print("\nTotal of numbers:",total)

# Q. Print the multiplication table of a number.

num = 6
print("\nNumber's table:")
for i in range(1,11):
    print(num * i)

# Q. Find the factorial of a number.
number = 5

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)


# Q. Count the number of digits in a number.

new_num = 1234

count = 0

while new_num > 0:
    new_num = new_num // 10
    count = count + 1

print("Number of digits:", count)

# Q. Reverse a number.

reverse = 0
while new_num > 0:
    digit = new_num % 10
    reverse = reverse * 10 + digit
    new_num = new_num // 10

print("Reversed number:", reverse)

# Q. Check whether a number is prime.

if new_num<= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, new_num):
        if new_num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

# Q. Print all prime numbers from 1 to 100.

for new_numb in range(2,101):
    is_prime = True

    for i in range(2,new_numb):
        if new_numb % i == 0:
            is_prime = False
            break
    if is_prime:
        print(new_numb)

# Q. Find the sum of digits of a number.

n = 12345
sum_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n = n // 10
print("sum_of_digits:", sum_of_digits)

# Q. Find the largest number among 10 user-entered numbers.
largest = None

for i in range(2):
    num = int(input("Enter a number:"))
    if largest is None or num > largest:
        largest = num

print("the largest number user entered is:", largest)

# Q. Keep asking for numbers until the user enters 0.

while True:
    num = int(input("enter the number:"))
    if num == 0:
        break
print("your entered number is matched with 0:",num)


# Q. print pattern 1 to 6 stars
for i in range(1,7):
    for j in range(i):
        print("*", end = "")
    print() 

# Q. print pattern 1 to 6 numbers

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end = "")
    print()

# Q. Print all numbers from 1 to 500 that are divisible by 7.

for i in range(1, 501):
    if i % 7 == 0:
        print(i)


counts = 0

for i in range(1,101):
    if i % 3 == 0:
        counts += 1
    
print("Count of numbers divisible by 3:", counts)

# Q. Print numbers from 1 to 10, but break the loop when the number is 7.

for i in range(1,10):
    if i == 7:
        break
    print(i)

