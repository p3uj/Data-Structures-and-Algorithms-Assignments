from array import *

def binary_search(found_num, num_search):
    low = 0
    high = len(elements) - 1
    mid = int(low + (high - low) / 2)
    while low <= high:
        if elements[mid] < num_search:  # If the condition is true, low will be placed beside mid on the right side.
            low = mid + 1
        elif elements[mid] == num_search:
            print(f"Sorted Array: {elements}")
            print(f"The element {num_search} is found!")
            found_num = 1
            return found_num    # Return the value of found_num to calling function
        else:   # High will be placed beside mid on the left side.
            high = mid - 1
        mid = int(low + (high - low) / 2)
    print(f"{num_search} is not found!\n")

def bubble_sort():
    swap = 1    # Assign value 1 to swap variable for the next statement.
    while swap:
        swap = 0    # In each iteration of the while loop, the swap value remains 0 (indicating no exchange occurs).
        for i in range(number_of_elements-1):
            if elements[i] > elements[i+1]: # Swap the two adjacent elements if the condition is true.
                elements[i], elements[i+1] = elements[i+1], elements[i]
                swap = 1    # Assign value 1 to swap (indicate there was an exchange).

if __name__ == "__main__":
    elements = array('i', [])   # Allocate storage for user-inputted values in an array.
    while len(elements) == 0:
        number_of_elements = int(input("Enter number of elements: "))
        if number_of_elements >= 3 and number_of_elements <= 5: # Execute within this if statement if the number_of_elements is 3 to 5.
            for i in range(number_of_elements):
                elements.append(int(input("Enter value: ")))    # Add all user's inputted values in an elements variable.
        else:   # Execute this if the number_of_elements is less than 3 or greater than 5.
            print("The elements is less than 3 or exceeded the maximum of 5!\n")

    bubble_sort()
    found_number = 0    # Assign value 1 to found_number variable for the next statement.
    while not found_number:
        number_search = int(input("Enter number to be searched: "))
        found_number = binary_search(found_number, number_search)   # Call binary_search method. Then store the return value to found_number.