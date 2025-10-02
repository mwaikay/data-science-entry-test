def find_and_replace(lst, find_val, replace_val):
    """
    Task 1 - Create a function that searches for all occurrences of a value (find_val)
    in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input 'lst' must be a list.")

    modified_lst = []
    for item in lst:
        if item == find_val:
            modified_lst.append(replace_val)
        else:
            modified_lst.append(item)
    return modified_lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:

# Scenario 1: Replacing numbers
list1 = [1, 2, 3, 4, 2, 2]
find_val1 = 2
replace_val1 = 5
result1 = find_and_replace(list1, find_val1, replace_val1)
print(f"Original list: {list1}, Find value: {find_val1}, Replace value: {replace_val1} -> Modified list: {result1}")

# Scenario 2: Replacing strings
list2 = ["apple", "banana", "apple"]
find_val2 = "apple"
replace_val2 = "orange"
result2 = find_and_replace(list2, find_val2, replace_val2)
print(f"Original list: {list2}, Find value: {find_val2}, Replace value: {replace_val2} -> Modified list: {result2}")
