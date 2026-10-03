# Q. Write a function to calculate the percentage of marks.
def calculate_percentage(marks_obtained, total_marks):
    percentage = (marks_obtained/total_marks) * 100
    return percentage 
print(calculate_percentage(450, 500))

# Q. Create a function to add two numbers.

def add_numbers(a,b):
    return a + b

result = add_numbers(20,30)
print(result)

# Q. Create a function to calculate average.

def avg(list_of_numbers):
    total = sum(list_of_numbers)
    avgerage = total / len(list_of_numbers)
    return avgerage

print(avg([2,34,45,76,8,7,9,8,98,56,56]))

# Q. Create a function to check even/odd.

def check_number(a):
    if a % 2 == 0:
        return "number is even"
    else:
        return "number is odd"

print(check_number(5))  

# Q. Create a function to check prime numbers.

def check_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = 16

if check_prime(number):
    print("Prime number")
else:
    print("Not a prime number")

# Q. Create a function to find the maximum of three numbers.

def find_max(a,b,c):
    if a > b and a > c:
        return "a is largest nummber"
    elif b > c and b > a:
        return "b is largest number"
    else:
        return "c is largest number"

print(find_max(2,5,3))

# Q. Create a function to calculate percentage.

def percentage(optained, total):
    percents = (optained/total) * 100
    return percents

print(percentage(435,500))

# Q. Create a function to calculate salary after deduction.

def calculate_salary(gross_salary, deduction_percent):
    deduction = gross_salary * deduction_percent / 100
    net_salary = gross_salary - deduction
    return net_salary

print(calculate_salary(50000, 10))

# Q. Create a function that accepts a list and returns its average.

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

print(calculate_average([3,65,76,87,35,34,65,9,88,77,87]))

# Q. Create a function that returns the largest value from a list.
def max_number(number):
    for i in number:
        number.sort
        largest_number = number[-1]
        return largest_number

print(max_number([34,65,78,65,67,87,99]))

# Q. Create a function that removes duplicates.

def drop_duplicates(num_list):
    set(num_list)
    return set(num_list)
print(drop_duplicates([1,2,3,4,3,4,5,7,8,9,8,5,4,5,6,3,2,3,5,6,7,8,9]))

# Q. Create a function to count vowels.

def count_vowels(char):
    count_vowel = 0
    for i in char:
        if i in 'aeiouAEIOU':
            count_vowel += 1
    return count_vowel        
print(count_vowels("programming"))

# Q. Create a lambda function to square a number.

square = lambda x: x * x
print(square(5))

# Q. Use lambda with map().

numbers = [2,3,4,5,6,7,8,9]

square1 = list(map(lambda x: x *  x, numbers))
print(square1)

print(list(map(lambda x : x + 2,numbers)))

# Q. Use lambda with filter().

print(list(filter(lambda x : x % 2 == 0,numbers)))

# Q. Use lambda with sorted().

print(sorted(numbers, key = lambda x : x))
