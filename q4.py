def string_reverse(s):
    """
    Task 1 - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s[::-1]

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# Scenario 1: "Hello World"
reversed_string_1 = string_reverse("Hello World")
print(f"Original: 'Hello World', Reversed: '{reversed_string_1}'")

# Scenario 2: "Python"
reversed_string_2 = string_reverse("Python")
print(f"Original: 'Python', Reversed: '{reversed_string_2}'")
