
"""
Task 5

I need to create two functions, multiply_myself and min_max_length

"""

def multiply_myself(target, times):
    """
    Multiplies a target value by itself a given number of times.
    If an error occurs, prints an error message instead of crashing.
    """
    try:
        result = 1
        for i in range(times):
            result = result * target
        print(target, "multiplied by itself", times, "times is equal to", result, ".")
    except:
        print("An error has occurred.")


"""
This function return a tuple that contains the minimum value, the maximum value and the number of elements in the list

"""
def min_max_length(numbers):

    return (min(numbers), max(numbers), len(numbers))

multiply_myself(2, 5)

numbers = [3, 7, 1, 9]
print(min_max_length(numbers))