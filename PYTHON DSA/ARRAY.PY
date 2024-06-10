# creating array by using list

arr = [1,2,3,5,4,8,6,9]
print(arr)

# by this way it gives functionality of changing values as well but in arrays we cannot change values as arrays are immutable 

from array import array

# by using array module we can create array

arr1= array('i',[1,2,3,6,5,4,8,5,6])

print(arr1)
print(type(arr1))
print(type(arr))

new_arr = [10,22,38,27,11];
print(type(new_arr))