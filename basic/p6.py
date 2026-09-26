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