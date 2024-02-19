from array import *
if __name__ == "__main__":
    given_elements = array('i', [6, 8, 67, 1, 78, 2, 9, 4, 22, 18, 30])
    print(f"Given Elements: {given_elements}")

    # Sorting unsorted elements using selection sort.
    for i in range(len(given_elements)):
        if i == 0:
            if given_elements[i] > given_elements[-1]:  # Swap the first element and last element if the condition is true.
                given_elements[i], given_elements[-1] = given_elements[-1], given_elements[i]
        for j in range(i+1, len(given_elements)):
            if given_elements[i] > given_elements[j]:   # Swap the two adjacent elements if the condition is true.
                given_elements[i], given_elements[j] = given_elements[j], given_elements[i]
    print(f"Sorted Elements: {given_elements}")