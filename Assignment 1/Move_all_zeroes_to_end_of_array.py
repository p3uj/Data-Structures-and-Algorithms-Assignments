from array import *
arr = array('i', [23, 0, 0, 7, 2, 0, 15, 45, 0, 32, 0, 57])
print(f"Original Elements: {arr}")
for i in range(len(arr)):   # Loop based on the total number of elements in the arr variable. In this case, 12.
    if arr[i] == 0:
        arr.remove(0)   # Remove the first 0 element in the arr variable.
        arr.append(0)   # Append/Add 0 in the end of the array elements.
print(f"Moved zeroes to end: {arr}")