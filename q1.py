def swap(x, y):
    """
    Task 1 - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swapping using arithmetic operations without a third variable
    x = x + y
    y = x - y
    x = x - y
    
    print(f"Swapped values: x = {x}, y = {y}")

# Task 2
# Invoke the function "swap" using the following scenarios:
print("Scenario 1: 'Apple', 10")
result1 = swap("Apple", 10)
if result1 == -1:
    print("Error: x and y must be numeric.")

print("\nScenario 2: 9, 17")
swap(9, 17)
