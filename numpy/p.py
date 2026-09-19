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

# Q. Create a NumPy array containing numbers from 10 to 100.

numpy_array = np.array(range(20,100))
print("\nnumpy array:",numpy_array)

# Q. Find the mean of all values greater than 50.

values = numpy_array[numpy_array > 50]
mean3 = np.mean(values)

print("\nmean of numbers which are greater than 50:",mean3)

# Q. Replace all negative values in an array with 0.

array5 = np.array([1,-3,4,-7,45,-4,635,5,-5,635,-35,7,76,-4,6,6,66,-46,6,67,6])

array5[array5 < 0 ] = 0

print("\nnew array:",array5)

# Q. Find the number of values that are: Greater than 50. Less than 20, Between 20 and 50.

print("\nnumbers are greter than 50 :",np.sum(array5 > 50))

print("numbers are less than 20:",np.sum(array5 < 20))

print("numbers are between 20 and 50:",np.sum((array5 > 20) & (array5 < 50)))

# Q. Create a 5×5 matrix and calculate the sum of its diagonal.

matrix = np.array(np.arange(25).reshape(5,5))
print("matrix:",matrix)

sum_diagonal = np.trace(matrix)
# also
sum_diag = np.sum(np.diag(matrix))

print("\nsum of diagonal:",sum_diagonal,"also", sum_diag)

# Q. Find the maximum value from each row of a NumPy matrix.

max_values = np.max(matrix, axis = 1)
print("\nmax of eaxh row:",max_values)

# Q. Find the minimum value from each column.

min_values = np.min(matrix, axis = 0)
print("\nmin value of each column:",min_values)

# Q. Create an array of 20 random integers between 1 and 100 and find:Mean, Median, Standard deviation, Maximum, Minimum.

array6 = np.random.randint(1,101,20)
print("array",array6)

mean_array = np.mean(array6)
median_array = np.median(array6)
std_array = np.std(array6)
max_array = np.max(array6)
min_array = np.min(array6)

print("\nmean: ",mean_array)
print("median:",median_array)
print("standerd deviation:",std_array)
print("maximum:",max_array)
print("minimum:",min_array)

# Q .Normalize this data:

data = np.array([10, 20, 30, 40, 50])

normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
print("\nnormalized data:",normalized_data)

# Q. Find the unique values and their frequency from a NumPy array.
unique_array = np.array([20,30,20,40,30,10,30,50,60,70,80,90,101,202,404,404,505,808,202,3,45,505])
print("\narray:",unique_array)

unique_values, frequency = np.unique(unique_array, return_counts = True)

print("\nunique values:",unique_values)
print("frequency:", frequency)
