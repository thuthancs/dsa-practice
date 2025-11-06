# 557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

- Input: s = "Let's take LeetCode contest"
- Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

- Input: s = "Mr Ding"
- Output: "rM gniD"

## Understand

- Input: a string
- Output: a string
- So, what I understand is that the white space is like a seperate and when you traverse through the string, if you encounter a white space, then you should reverse everything that comes before (i.e., the individual word).

## Match

Because we have to reverse the words, a **two-pointer** approach seems appropriate here.

## Plan

- First, I need to transform the string into a list of characters: s = list(s)
- Then, I will create a helper function to perform the reversal operation: helper(l, r)
- Initialize l = 0
- Then, I need to loop through the list and check the following conditions:
  - If the char at the current index is an empty space: pass in the helper r = i - 1 and l
  - Then, update l to l += i + 1
- Continue until the end of the list

## Implement
### First Attempt
- Failed a test case:
```
Output: "Let's take LeetCode contest"
Expected: "s'teL ekat edoCteeL tsetnoc"
```
```
def reverse_words(s):
    def helper(l, r):
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    l = 0
    s = list(s)
    n = len(s)

    for r in range(n):
        if s[r] == " ":
            helper(l, r - 1)
            l += r + 1 # the problem is here, over-increment l
        elif r == n - 1:
           helper(l, r)

    return "".join(s)
```
### Second Attempt
- Just simply update l to be equal to r + 1, not increment it by r+1

## Review

- Learning from my mistake in the previous problem, I will not pass in substring to the helper function.
- Let's dry run through a small example: s = "Mr Ding"
- l = 0, s = ["M", "r", " ", "D", "i", "n", "g"], n = 7
- r = 0 and s[r] != " ", continue until r = 2, s[r] == " "
  - l = 0, r = 2 (oh we need to subtract by 1 here so r = 1), swap and we have s = ["r", "M", " ", "D", "i", "n", "g"]
- Update l = 2 + 1 = 3
- Continue incrementing r but because there's no space at the end so it will not be swapped so I need to add another condition to swap the last string.

## Evaluate

- Time Complexity: O(n)
- Space Complexity: O(n)
