# Coding Interview - Data Structures & Algorithms Patterns
This repo consists of my own categorization of coding interview questions. I collected these questions from multiple sources, primarily LeetCode and books such as Elements of Programming Interviews, Cracking the Coding Interview, and Beyond Cracking the Coding Interview. I like to group the questions under a prominent theme and break them down further into data structures and common techniques. 

I organize the questions in order, meaning **you need to solve them in the order presented**, because subsequent questions are built upon the answers to those that come before. For some patterns that utilize the same data structure, such as trees, I also intentionally organize them in order (e.g., you need to know how to traverse a tree before learning how to search for a specific value in the tree). This approach helps me reinforce my understanding and notice repeated mistakes I make under the same theme.

# 📘 Table of Contents
- [Reversal Pattern](#reversal-pattern)
  - [Two Pointers](#two-pointers)
    - [String](#string)
    - [Linked List](#linked-list)
- [Tree Traversal Pattern](#tree-traversal-pattern)
  - [Breadth-first Search (BFS)](#breadth-first-search)
  - [Depth-first Search (DFS)](#depth-first-search)
- [Search in Trees Pattern](#search-in-trees-pattern)

# Reversal Pattern
> Reversal pattern often asks you to **change the order of items or swap them** in different data structures.
## Two Pointers 
### String
- [344. Reverse String](https://leetcode.com/problems/reverse-string/description/)
- [541. Reverse String II](https://leetcode.com/problems/reverse-string-ii/description/)
- [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/description/)
- [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/description/)
  
Common pitfalls I made so you don't have to: 
- Forgot to convert a string into a list before performing the swap. Because a string is immutable, we cannot modify it directly.
- Forgot to use a while loop for the swapping logic, but used an `if` statement, so the swapping only occurs once.
- Once in a while, did not handle the index and the bounds of the index well, so got the error of list index out of range.
  
### Linked List
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/description/)
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)
- [2074. Reverse Nodes in Even Length Groups](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/description/)
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/)
- [1721. Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/)

Common pitfalls I made so you don't have to:
- The trickiest part of reversing a linked list is to keep track of the reassignment of the head/left nodes and right/end nodes. The best solution I found for this problem is to visualize/draw every step out for the first few problems that you do, instead of just half-dry-running the example. You must internalize the reassignment mechanism before you can proceed to more complex problems.
- Carefully read the problem to see whether it asks you to swap the values only or to change the pointers/references of the nodes.

# Tree Traversal Pattern
## Breadth-first Search
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
- [429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/)
- [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)
- [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/)
## Depth-first Search
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)
- [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/)
- [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/)

# Search in Trees Pattern
- [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)
- [270. Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/description/)
- [272. Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/)
- [2476. Closest Nodes Queries in a Binary Search Tree](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/description/)
