def max_subarray_and_sum(array):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum, start_index, end_index = 0, 0, 0

    for i in range(len(array)):
        if current_sum < 0: # If current_sum becomes negative, reset it based on the value in array[i]
            current_sum = array[i]
            start_index = i
        else:
            current_sum += array[i]

        if current_sum > max_sum:   # Update max_sum
            max_sum = current_sum
            end_index = i
    return array[start_index:end_index + 1], max_sum

def main():
    try:
        number_of_elements = int(input("Enter the number of elements (max: 10): "))
        if number_of_elements >= 1 and number_of_elements <= 10:    # Check if the number_of_elements is between 1 to 10.
            array_elements = []
            for i in range(number_of_elements): # User input
                array_elements.append(int(input("Enter an integer element: ")))

            max_subarray, max_sum = max_subarray_and_sum(array_elements)    # Compute maximum subarray and sum

            # Print the result
            print(f"\nArray: {number_of_elements}")
            print(f"Maximum subarray: {max_subarray}")
            print(f"Maximum sum: {max_sum}")
        else:
            print("Element number must be between 1 and 10!")
    except ValueError:
        print("Invalid input!")

if __name__ == "__main__":
    main()