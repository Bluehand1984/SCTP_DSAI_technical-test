def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    if not isinstance(lst, list):
        raise ValueError("Not a list")

    index = 0  # Initialize list pointer
    
    while index < len(lst):  #worst case loop until total number of elements in list.
        if lst[index] < 0:  #no error handling here
            return lst[index]  # Return the first negative number
        index += 1  # Move to the next index
    
    return "No negatives"  


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))
#print(find_first_negative([0, 0, 0, 0, 0, -8]))
#print(find_first_negative([0, 0, 0, 0, 0, 0]))
#print(find_first_negative([0, 0, 0, "a", 0, -8]))
