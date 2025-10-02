def check_divisibility(number, divisor):
    """
    Task 1 - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(number, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both 'number' and 'divisor' must be numeric.")
    
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")

    return number % divisor == 0

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print(f"Is 10 divisible by 2? {check_divisibility(10, 2)}")
print(f"Is 7 divisible by 3? {check_divisibility(7, 3)}")
