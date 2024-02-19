from array import *
arr = array('i', [20, 30, 89, 1, 67, 44, 78])
print(f"Original Array: {arr}")

sorted_arr = array('i', sorted(arr))    # Sort the elements in arr variable then convert it to array.
print(f"Sorted Array: {sorted_arr}\n")

print("Largest Elements:")
largest_element = 1   # Initialize largest_element to 1 for preparation to the for loop statement.
for i in range(3):
    print(sorted_arr[-largest_element]) # Print one element at a time in the sorted_arr variable staring from the right side to left.
    largest_element+=1  # Increment the value of largest_element for preparation to the next loop.