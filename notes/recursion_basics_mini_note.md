# Recursion Basics Mini Note

Recursion means a function calls itself.

A recursive function needs two things:

1. Base case
2. Recursive call

The base case stops the recursion.

The recursive call makes the problem smaller.

Example:
If I want to count down from 5, I print 5, then call the same function with 4, then 3, then 2, then 1.

Main idea:
Recursion solves a problem by breaking it into smaller versions of the same problem.

## Base Case

The base case is the stopping condition.

Without a base case, recursion will continue forever.

Example:
if n == 0:
    return

## Recursive Call

The recursive call is when the function calls itself with a smaller input.

Example:
countdown(n - 1)

This moves the problem closer to the base case.