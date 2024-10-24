def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    
    # Slicing from end
    r_string = s[::-1]
    
    return r_string


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print(string_reverse("Hello World"))
print(string_reverse("Python"))
