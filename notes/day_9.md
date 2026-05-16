# Day 9 Progress

Today I studied **binary search basics**, reviewed important algorithm theory topics, and solved **Search Insert Position**.

## Theory studied

Today I cleaned up some important CU Boulder preparation topics:

```text
Big-O notation
Sorting basics
Selection sort
Merge sort
Quick sort
Recursion basics
Base case
Recursive call
Binary search basics
```

I learned that sorting and searching are connected. If an array is sorted, I can use binary search instead of checking every value one by one.

## Sorting concepts

I understood the basic ideas of three sorting algorithms:

```text
Selection Sort:
Repeatedly find the smallest value and place it in the correct position.

Merge Sort:
Split the array into smaller halves, then merge the sorted halves back together.

Quick Sort:
Choose a pivot, place smaller values on one side and bigger values on the other side.
```

Main lesson:

```text
Sorting makes data easier to search.
```

## Recursion concepts

I also studied recursion basics.

Main idea:

```text
Recursion means a function calls itself to solve a smaller version of the same problem.
```

Every recursive function needs:

```text
1. Base case
2. Recursive call
```

The base case stops the recursion.
The recursive call moves the problem closer to the base case.

This is important because algorithms like merge sort and quick sort use recursive thinking.

## Problem solved: Search Insert Position

Today I solved **Search Insert Position**.

In this problem, I had to find the index of a target value in a sorted array. If the target did not exist, I had to return the index where it should be inserted.

At first, I tried to think about splitting the array from the middle, but I made mistakes by trying to move `mid` directly. Then I understood that in binary search, I should not manually move `mid`.

The correct thinking is:

```text
left = start of the search area
right = end of the search area
mid = middle of the current search area
```

If the target is smaller than `nums[mid]`, I move `right`.

If the target is bigger than `nums[mid]`, I move `left`.

Then `mid` is recalculated again from the updated `left` and `right`.

Main lesson:

```text
Do not move mid directly.
Move left or right.
Then recalculate mid.
```

## Important binary search idea

If the target is found, return `mid`.

If the target is not found, return `left`.

This is because after the binary search ends, `left` becomes the correct insert position.

## Main lessons

```text
- Binary search only works properly on sorted arrays.
- Binary search cuts the search space in half each time.
- left and right control the search boundary.
- mid is calculated from left and right.
- I should update left or right, not mid directly.
- If target is not found in Search Insert Position, return left.
- Binary search is faster than linear search for sorted arrays.
```

Pattern learned:
Binary Search

Problem added to tracker:
Search Insert Position

Big-O understanding:

```text
Time Complexity: O(log n)
Space Complexity: O(1)
```

Project improvement:

```text
Added Search Insert Position to the DSA Tracker and pushed the update to GitHub.
```

Reflection:

Today I understood binary search more clearly. At first, I was trying to move from the middle outward, but then I realized that binary search starts with the whole search area and removes half of it each time. This helped me understand the role of `left`, `right`, and `mid`. I also completed important theory notes on sorting and recursion, which will help me prepare for CU Boulder algorithms.

Extra Progress: Contains Duplicate II

Today I also solved Contains Duplicate II. This problem extended my understanding of Contains Duplicate. Instead of only checking whether a value appeared before, I had to check whether the duplicate appeared within distance k.

Main idea:
Store each number’s latest index in a dictionary. If the same number appears again, calculate the distance between the current index and the previous index. If the distance is less than or equal to k, return True.

Pattern:
Hash Map / Index distance checking

Time Complexity: O(n)
Space Complexity: O(n)


