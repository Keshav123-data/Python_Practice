# Q. Remove duplicate values from a list.
list1 = [1,2,3,2,3,4,2,3,1,2,4,2,3,1,4]
list1 = list(set(list1))
print(list1)


list2 = ["a","b","c","a","c","b","b","a","c"]
list2 = list(set(list2))
print(list2)

# Q. Find the second-largest number in a list.
list = [10,230,3540545,505050,453993,94,95405495]
list.sort()
second_largest = list[-2]
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