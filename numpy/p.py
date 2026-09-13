# Q. Create a NumPy array containing numbers from 1 to 20.
import numpy as np

list1 = [1,2,3,4,5]

result = []

for i in list1:
    result.append(i)
print(result)
print(type(result))

# lets convert into iin array
result_array = np.array(result)
print(result_array)

# lets check  
print(type(result_array))

array = np.arange(1,21)
print(array)

# Q. Calculate mean, median, standard deviation, minimum, and maximum.
array1 = np.array([10,20,7,30,80,40,30,60,89])

mean = np.mean(array1)
median = np.median(array1)
std = np.std(array1)
min = np.min(array1)
max = np.max(array1)

print("mean:", mean)
print("median:", median)
print("standard deviation:", std)
print("min:", min)
print("max", max)


# Q. Replace all values greater than 50 with 50.
import numpy as np 
array2 = np.array([40,50,20,70,40,60,80,90,200,40,60,23,40,10])

array2[array2 > 50] = 50
print(array2)

# Q. Find the indexes of values greater than 100.
array3 = np.array([20,150,40,30,100,50,100,70,200,60,100,200,500])

indexes = np.where(array3 >= 100)[0]

print(indexes)

# Q. Reshape a 1D array into a 3×4 matrix.
d1array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(d1array.shape)

# lets reshape it to 2d array
d2array = d1array.reshape(3,4)
print(d2array)
print(d2array.shape)

# Q. Calculate the sum of each row and each column.

arr = np.array([
    [20,50,30],
    [90,40,10],
    [60,30,80],
    [70,80,90]
])

row_sum = np.sum(arr, axis = 1)
column_sum = np.sum(arr, axis=0)

print("sum of rows:",row_sum)
print("sum of columns:",column_sum)

# Q. Normalize an array using (x - mean) / std.
ar= ([4,6,3,6,8,7,4,3,6,8,3])

mean1 = np.mean(ar)
std1 = np.std(ar)

normalized = (ar - mean1) / std1

print("mean:",mean1)
print("std:",std)
print("normalized:",normalized)

# Q. Find duplicate values in a NumPy array.
array4 = ([1,2,4,3,2,1,2,4,4,3,2,1,2,3,4,2,2])

values, counts = np.unique(array4, return_counts = True)

duplicates = values[counts > 1]

print(duplicates)

# Q. Generate 100 random numbers and calculate their statistics.
rdm_array = np.random.randint(1,101,100)

mean2 = np.mean(rdm_array)
median2 = np.median(rdm_array)
std2 = np.std(rdm_array)
min2 = np.min(rdm_array)
max2 = np.max(rdm_array)

print("array:",rdm_array)
print("mean:",mean2)
print("median:",median2)
print("std:",std2)
print("min:",min2)
print("max:",max2)


# Q. Filter an array based on multiple conditions.

arra = np.arange(1,21)
print("array:",arra)

filtered = arra[(arra > 5) & (arra < 16)]
print("filtered array:",filtered)