"""
Question 1: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

1. Clarify - So you want me to create a function that takes in a non-empty array of numbers, only integers
and return the single integer that doesn't appear twice?

2. Assumptions - I will assume that the array has only integers and nothing else in it, ie. string, floats, objects, ects. 
I will assume that the function needs to return a single integer in the array, and not a boolean. And only one integer in the array appears once

3. The brute force way of doing this would be to compare every single value against each other and if see if they match and only returning the value with out a match.
Hence, the unique value. To slove this problem this problem with a better runtime I would iterate over the given array 
and append to a new array if the value is not in the new array, otherwise if it's in the list 
then remove it from the new list and return the single value the new array, but since the I created the new array
it will return it as a list and to return a single integer I can use the pop method on the returned array.

4. Examples of assumption - So for example if I am given an array like a = [2, 3, 2, 1, 3], I am to return 1
"""

def find_unique(array):

    unique_list = []

    for i in array: 
        if i not in unique_list:
            unique_list.append(i)
        else:
            unique_list.remove(i)

    return unique_list.pop()


"""
Question 2: Given an integer, write a function to check whether it is a power of 4.

1. Clarify - I need to create a function that return a boolean of whether the input as an integer is the power of 4? Will zero be a valid integer?

2. Assumptions - I will assume that the input will be an integer and not a float or string or any other data type. I will assume to 
return a true or false boolean.

3. To solve this problem I would create a new variable to hold the integer and use python's floor division operator of 4, 
and updating the new number's value with a while loop, until the new number's value it less than 0. Finally, at the end I would 
check to see if there's any remainder for the new number if so, then return False, because it's not totally  divisible by 4 meaning it's not the
power of 4 and conversely, return True, because there are no remainder 

4. Examples of assumption - If I am given an interger of 64, function should return true, if the integer is 63, function should return false
"""

def is_power_of_4(n):
    new_number = n

    while new_number > 0:
        new_number -= n // 4
    
    if new_number == 0:
        return True
    else:
        return False



if __name__ == '__main__':
    test_array = [2, 3, 2, 1, 3]
    print(find_unique(test_array))

    integer = 64 # True
    integer2 = 63 # False
    print(is_power_of_4(integer))
    print(is_power_of_4(integer2))