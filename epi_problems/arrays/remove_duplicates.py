"""Remove duplicates in a sorted array

Write a program that takes as input a sorted array and updates it so that all duplicates have been removed and the remaining elements
have been shifted left to fill the emptied indices. Return the number of valid elements.

Example: Given the array: A = [2,3,5,5,7,11,11,11,13], after deletion, the array is [2,3,5,7,11,11,11,13]. After deleting repeated elements,
there are 6 valid entries which are [2,3,5,7,11,13]
"""


def remove_duplicates(arr):
    count = 1
    existing_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != existing_val:
            existing_val = arr[i]
            count += 1

    return count


A = [2, 3, 5, 5, 7, 11, 11, 11, 13]
print(remove_duplicates(A))
