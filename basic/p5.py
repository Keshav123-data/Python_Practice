# Q. 5 Calculate the average of numbers in a list.
list = [1,2,5,3,6,8,5,4]
sum1 = 0
for i in list:
    sum1 += i
average = sum1 / len(list)
print(average)

list1 = [2,5,3,6,8,6,4,3,5,67,8,6,43,3,55,768,8,54,3,45]
average1 = sum(list1)/len(list1)
print(average1)