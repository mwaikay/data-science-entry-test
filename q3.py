def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print(f"Original value for key '{key}': {dct[key]}")
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:

# Scenario 1: Empty dictionary, adding a new key-value pair
dict1 = {}
updated_dict1 = update_dictionary(dict1, "name", "Alice")
print(f"Updated dictionary 1: {updated_dict1}")

# Scenario 2: Dictionary with an existing key, updating its value
dict2 = {"age": 25}
updated_dict2 = update_dictionary(dict2, "age", 26)
print(f"Updated dictionary 2: {updated_dict2}") 
