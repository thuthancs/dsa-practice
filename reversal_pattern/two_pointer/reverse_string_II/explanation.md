# 541. Reverse String II

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:

- Input: s = "abcdefg", k = 2
- Output: "bacdfeg"

Example 2:

- Input: s = "abcd", k = 2
- Output: "bacd"

## Understand

- Input: a string (s) and an integer (k)
- Output: a string
- For example, given the input s = "abcdefg" and k = 2, I will first need to consider the first 4 characters (2\*2 = 4) = "abcd". Then, I will reverse the first 2 characters to become "bacd". Then, I continue to consider "feg" and because 2 < len("feg") < 4, I reverse the first two characters to get "efg". The final result would be "bacdfeg".
- Edge cases: I can assume that the input is always valid (meaning it's not empty)

## Match

Because it has to do with reversal, I think we can use **two-pointer** approach in this case.

## Plan

- First, convert the string into a list of characters so that we can actually swap their positions: s = list(s)
- Then, create a helper funtion to perform the reversal operation for a substring: reverse(st)
- Then, initialize the left and right pointer as: l = 0, r = 2\*k - 1
  - Check if the length of the substring is < 2k but > k: reverse the first k
  - Check if the length of the substring is < k: reverse them all

## Implement

### First Attempt

```python
def reverse_string(s, k):
    def helper(s, l, r):
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    s = list(s)
    r = 2*k - 1

    for i in range(0, len(s), 2*k):
        if r - i > k and r - i <= 2*k:
            helper(s[i:i+k], i, i+k)
        elif r - i < k:
            helper(s[i:r+1], i, r)
        r += 2*k - 1

    return ''.join(s)
```

### Second Attempt

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)

        def helper(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        for i in range(0, n, 2*k):
            if len(s[i:]) < k:
                helper(i, n-1)
            else:
                helper(i, i + k -1)

        return "".join(s)
```

## Review

- My original attempt returned "list index out of range" error because the indices got messed up when I tried to pass in the substring that needs to be swap. If the substring has a length of 2 and the left pointer is 4 and the right pointer is 6, then the error occurs. As a result, passing the substring is not a good idea.
- Then I realized that I could just use the original array of string and update the left and right pointer as I go. It turned out to be pretty simple.

## Evaluate

- Time Complexity: O(n) because of the operation that transforms a string into a list of characters, and the swapping operation takes at max O(N // k) operations, same as the for loop
- Space Complexity: O(n) because of the array that is used to store all the letters of the string
