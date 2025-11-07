# 345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation: The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

## Understand

- Input: a string
- Output: a string
- Based on the examples, I can see that in the first case where s = "IceCreAm", the vowels are "I", "e", "e", "A", so we reverse all of them to get "AceCreIm" - A should be first because in the original string, it's the last one. In the second example where s = "leetcode", the vowels are "e", "e", "o", "e", and we reverse all of them.

## Match

- Because the task requires reversal, a **two-pointer** approach would work best here

## Plan

- First, transform the string into a list of characters
- Next, create a list of vowels: lower_vowels = ["u", "e", "o", "a", "i"], upper_vowels = [v.upper() for v in lower_vowels], vowels = lower_vowels + upper_vowels
- Then, initialize the left pointer as 0 and right pointer as n - 1
- Then, create a while loop such that when l < r, we check:
  - If s[l] is a vowel and s[r] is a vowel, swap them
  - If s[l] is not a vowel and s[r] is, increment l by 1
  - If s[l] is a vowel and s[r] is not, decrement r by 1
  - Else, increment l and decrement r

## Implement

```python
def reverse_vowels(s):
    lower_vowels = ["u", "e", "o", "a", "i"]
    upper_vowels = [v.upper() for v in lower_vowels]
    vowels = lower_vowels + upper_vowels

    s = list(s)
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] in vowels and s[r] in vowels:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        elif s[l] in vowels and s[r] not in vowels:
            r -= 1
        elif s[r] in vowels and s[l] not in vowels:
            l += 1
        else:
            l += 1
            r -= 1

    return "".join(s)
```

## Review

- Let's dry run through an example: s = "leetcode"
- l = 0, r = 7
- because s[0] = l not in vowels and s[7] = e in vowels, l += 1 = 1
- s[1] = e and s[7] = e are vowels, swap and l = 2, r = 6
- s[2] = e in vowels and s[6] = d not in vowels, l = 2, r = 5
- continue

## Evaluate

- Time complexity: O(n)
- Space complexity: O(n)
