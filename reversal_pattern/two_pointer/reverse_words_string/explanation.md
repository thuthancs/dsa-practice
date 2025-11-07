# 151. Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the   sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = " hello world "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

## Understand

- Input: a string with potentially multiple spaces and trailing spaces
- Output: a single-spaced string without trailing spaces

## Match

- Because we need to reverse the words, a **two-pointer** approach would work best here

## Plan
- First, we need to remove any trailing spaces from the original string
- Initialize start pointer as 0
- Initialize an empty list: []
- Loop through the original string and if s[i] is a space, slice the substring s[start:i] and add it to the empty list
- Update the start pointer to start += i
- Continue until i = n - 1, add the last word to the empty list
- Create a helper function to do the reverse of the list
- Then join them together with a single space

## Implement
```python
def reverse_words(s):
    s = s.strip()
    start = 0
    words = []
    for end in range(len(s)):
        if end == " " and s[end + 1] != " ":
            word = s[start:end].rstrip()
            words.append(word)
            start += end
        elif end == n-1:
            word = s[start:end].rstrip():
            words.append(word)
    
    l, r = 0, len(s) - 1
    while l < r:
        words[l], words[r] = words[r], words[l]
    
    return " ".join(words)

```

## Review

## Evaluate
