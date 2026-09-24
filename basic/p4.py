# Q.4 Count how many even numbers are present in a list.

list = [1,2,3,4,5,6,7,8,9]
count = 0
for n in list:
    if n % 2 == 0:
        count += 1
print("Count of even number in the list is:", count)

# Q.4a Count how many odd numbers are present in a list.
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
