def find_first_negative(lst):
    """
    Task 1 - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    index = 0
    while index < len(lst):
        # Attempt to convert the element to an integer to handle string representations of numbers
        try:
            current_element = int(lst[index])
            if current_element < 0:
                return current_element
        except ValueError:
            # If conversion fails, it's not a number, so skip it
            pass
        index += 1
    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenarios:

# Scenario 1
list_one = [3, 5, "-1", 7, "-2", 8]
result_one = find_first_negative(list_one)
print(f"First negative in {list_one}: {result_one}")

# Scenario 2
list_two = [2, 10, 7, 0]
result_two = find_first_negative(list_two)
print(f"First negative in {list_two}: {result_two}")
