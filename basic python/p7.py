# Q.7 Count the frequency of each element in a list.
list1 = [1,2,3,1,3,4,6,4,3,1,3,4,4,5,4,3,2,3,4,5,4,3,2]
frequency = {}
for i in list1:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)