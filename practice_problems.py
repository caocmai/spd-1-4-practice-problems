"""
Question 1: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

1. Clarify - So you want me to create a function that takes in a non-empty array of numbers, only integers
and return the single integer that doesn't appear twice?

2. Assumptions - I will assume that the array has only integers and nothing else in it, ie. string, objects, ects. 
I will assume that the function needs to return a single integer in the array, and not a boolean. And only one integer in the array appears once

3. So to do this I would iterate over the given array and append to a new array if the value is not in the new array, otherwise if it's in the list 
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
Question 2: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

1. Clarify - So you want me to create a function that takes in a non-empty array of numbers, only integers
and return the single integer that doesn't appear twice?

2. Assumptions - I will assume that the array has only integers and nothing else in it, ie. string, objects, ects. 
I will assume that the function needs to return a single integer in the array, and not a boolean. And only one integer in the array appears once

3. So to do this I would iterate over the given array and append to a new array if the value is not in the new array, otherwise if it's in the list 
then remove it from the new list and return the single value the new array, but since the I created the new array
it will return it as a list and to return a single integer I can use the pop method on the returned array.

4. Examples of assumption - So for example if I am given an array like a = [2, 3, 2, 1, 3], I am to return 1
"""



if __name__ == '__main__':
    test_array = [2, 3, 2, 1, 3]
    print(find_unique(test_array))