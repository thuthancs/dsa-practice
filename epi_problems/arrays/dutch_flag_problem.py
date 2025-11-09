"""The Dutch Flag Problem

Write a program that takes an array A and an index i into A and rearranges the elements such that all elements less than A[i] (the pivot)
appear first, followed by elements equal to the pivot, followed by elements greater than the pivot.

Example:
A = [0, 1, 2, 0, 2, 1, 1]
If the pivot index is 3 where A[3] = 0. A valid partitioning would be: A = [0, 0, 1, 2, 2, 1, 1]. Why? Because we want to put all the
elements that is equal or less than A[i] before i = 3 (e.g., all the 0s and 1s) and all the elements that are greater than A[i]
after the index = 3.

If the pivot index is 2 where A[2] = 2. A valid partitioning would be: A = [0, 1, 0, 1, 1, 2, 2] or A = [0, 0, 1, 1, 1, 2, 2] because all
the elements before index 2 is < 2.

- Thoughts: I think the instruction is a bit vague like I'm not sure if the order of the values after the pivot also has to follow
a speciific order or not. Okay so I get it now. The key thing here is that all of the elements that are less than the pivot value should
come before it and the remaining should come after it and we don't really care about the order of the remaining portion. This explains why
when the pivot is 3 (A[3] = 0), the valid partitioning is when all the 0s come first in the array and what comes after that are all the
1s and 2s with not ordering. Similarly, in the second case where pivot index = 2 (A[2] = 2), a valid partitioning is where all the 0s and 1s
come before 2 (ordering does not matter) and all the 2s are rearranged at the end of the array.
"""


# FIRST ATTEMPT: Using a while loop
def partition(arr: list[int], pivot: int):
    idx = 0
    curr_val = arr[pivot]
    while idx < len(arr):
        if arr[idx] > curr_val:
            arr[idx], arr[pivot] = arr[pivot], arr[idx]
        if idx > pivot:
            if arr[idx] < arr[pivot]:
                arr[idx], arr[pivot] = arr[pivot], arr[idx]
        idx += 1
    return arr


A = [0, 1, 2, 0, 2, 1, 1]
# print(partition(A, 3))
# print(partition(A, 2))


# SECOND ATTEMPT: Two passes loop
def valid_partition(arr, pivot):
    pivot_val = arr[pivot]
    n = len(arr)
    smaller = 0
    for i in range(n):
        if arr[i] < pivot_val:
            arr[smaller], arr[i] = arr[i], arr[smaller]
            smaller += 1

    larger = n - 1
    for j in range(
        n - 1, -1, -1
    ):  # REMEMBER: goes from n - 1 or else list index out of range, and ends at -1 because -1 - (-1) = 0 (which is the beginning of the loop)
        if arr[j] > pivot_val:
            arr[larger], arr[j] = arr[j], arr[larger]
            larger -= 1

    return arr


print(valid_partition(A, 3))
print(valid_partition(A, 2))
