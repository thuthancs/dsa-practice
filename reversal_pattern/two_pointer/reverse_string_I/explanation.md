# Reverse String

https://chatgpt.com/share/68d5ad36-2034-8008-8a2c-7883a3fba603

> Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Understand

- Input: array of strings
- Output: array of strings
- **Edge cases:**
  - Single-item list or empty list: return the list itself
  - The list consists of all the same characters: return the list itself
- **Requirements:**
  - Modify the input in-place
  - O(1) extra memory

## Match

- Because I cannot create an extra data structure to store the output, I need to solve the problem recursively.
- This problem has to do with swapping characters, so I think a two-pointer approach can also be applied here.
- In general, the solution will be a combination of **recursion and two pointers**.

## Plan

![Figure 1. Visualization of what I thought the solution should be.](/recursion/diagram.png)

Figure 1. Visualization of what I thought the solution should be.

- First, the base case here is when there is only 1 character (no reversion is needed). This is equivalent to when l == r.
  - We have to break the problem down until it reaches the base case by incrementing the left pointer and decrementing the right pointer until they are equal or when left > right.
- Return the solution for the base case
- Swap the positions of the left and right pointers in the bigger problem that already consists of the base case as the solution
- Return the solution for this subproblem
- Swap the positions of the left and right pointers in the bigger problem that already contains the solution for the previous subproblem.

## Implement

### 1st Attempt

> **TL;DR:** The base case is not necessarily a value that needs to be returned. It can be a stopping point with just a return that tells the program to stop running! I’m still confusing when to return a value inside the recursive call. Make sure to pay attention to what is actually returned at each call.

```python
def reverse_string(s):

	def helper(l, r):
		if l == r:
			return s[l]
		elif l > r:
			s[l], s[r] = s[r], s[l]
		else:
			return helper(l + 1, r - 1)

	if len(s) == 1 or len(s) == 0:
		return s

	l, r = 0, len(s) - 1
	return helper(l, r)
```

- If you look at the helper function, you can see that it only returns the base case.
  - For example, given the string “cat”, we have l = 0 and right = 2.
  - We pass these two parameters into the helper function.
  - Because l ≠ r, we call the helper function on a smaller subproblem: helper(1, 1) → then it just returns the base case “a” without changing anything
- If we change it to, meaning we do not return anything from the helper function, but just call it to modify the string in place:
  ```python
  if l == r:
      return s[l]
  elif l > r:
      s[l], s[r] = s[r], s[l]
  else:
      helper(l + 1, r - 1)
  ```
  - It’s the same problem because it will keep breaking things down until l == r and return s[l] only, and on the recursive call of the bigger problem helper(l+1, r-1), nothing is returned!
- Then, if we change the second condition to swap the left and right pointers when r > l, then the problem is that the swap is only performed once on the first pass, and nothing is returned on the second conditional statement!
  ```jsx
  if l == r:
      return s[l]
  elif l > r or r > l:
      s[l], s[r] = s[r], s[l]
  else:
      helper(l + 1, r - 1)
  ```

### Second Attempt

![Figure 2. Correct implementation](/recursion/revised_diagram.png)

```python
def reverse_string(s):
	def helper(l, r):
		# base case: when l >= r, stop the recursion
		if l >= r:
			return
		else:
			# swap the positions of two characters
			s[l], s[r] = s[r], s[l]

			# recurse inwards
			helper(l+1, r-1)

		l, r = 0, len(s) - 1
		return helper(l, r)
```

### Iteration

```python
l, r = 0, len(s) - 1
while l < r:
	s[r], s[l] = s[l], s[r]
	l += 1
	r -= 1
return s
```

## Review

- The solution works for all cases, actually, I don’t need the conditions to check whether the list only consists of 1 item or no items at all.

## Evaluate

### Recursion

- Time Complexity: O(N) because of N/2 swaps
- Space Complexity: O(N) because of the recursion stack. Specifically, if we have a list size of n, then we need to make N/2 recursive calls to perform the swapping, which takes N/2 space, which can be generalized as O(N)

### Iteration

- Time Complexity: O(N) because of N/2 swaps
- Space Complexity: O(N) because no space is needed to store the output
