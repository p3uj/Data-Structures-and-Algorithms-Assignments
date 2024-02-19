from array import *

def find_largest_element():
    largest_element = array_elements[0] # Assume that the first largest element is in the index 0.
    for i in range(1, number_of_elements):
        if largest_element < array_elements[i]: # Compare and check the larger element.
            largest_element = array_elements[i] # Assign the latest largest element.
    print(f"Largest Element: {largest_element}")

if __name__ == "__main__":
    array_elements = array('i', []) # Allocate storage for user-inputted values in an array.
    while len(array_elements) == 0:
        number_of_elements = int(input("Enter number of elements: "))
        if number_of_elements >= 5 and number_of_elements <= 10: # Execute within this if statement if the number_of_elements is 5 to 10.
            for i in range(number_of_elements):
                array_elements.append(int(input("Enter value: ")))    # Add all user's inputted values in an array_elements variable.
        else:   # Execute this if the number_of_elements is less than 5 or greater than 10.
            print("The elements of an array is less than 5 or exceeded the maximum of 10!\n")
    find_largest_element()