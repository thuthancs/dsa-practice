"""Compute an alteration

Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array B having the property that
B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ...

Example:
A = [1, 2, 3, 4, 5, 6]
output = [1, 3, 2, 5, 4]
A[i-1] <= A[i] >= A[i+1]

A = [4, 5, 2, 7, 8]
output = [2, 5, 4, 8, 7]
"""


def alternate(arr):
    for i in range(1, len(arr)):
        if (i % 2 == 1) and (arr[i - 1] > arr[i]):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
        elif (i % 2 == 0) and (arr[i - 1] < arr[i]):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]

    return arr


print(alternate([1, 2, 3, 4, 5, 6]))
