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

