# Day 8 Progress

Today I solved **Maximum Subarray**, **Remove Element**, and **Remove Duplicates from Sorted Array**. This was a strong day because I practiced three important array patterns: **running sum**, **in-place update**, and **two-pointer overwrite position**.

## Problem 1: Maximum Subarray

In **Maximum Subarray**, I learned the running sum idea, also known as **Kadane’s Algorithm**.

At first, I was thinking about adding numbers one by one using a running sum. Then I realized that I do not need to store every possible subarray. I only need to track two values:

```text
current_sum = the sum I am building right now
max_sum = the best sum I have found so far
```

The important lesson was that the order matters. I must update `max_sum` before resetting `current_sum`. If `current_sum` becomes negative, I reset it to `0` because a negative running sum will hurt the next subarray.

Main lessons:

* Maximum Subarray asks for the best continuous subarray sum.
* A subarray must be continuous.
* I do not need to store all subarrays.
* `current_sum` tracks the sum I am currently building.
* `max_sum` tracks the best sum found so far.
* If `current_sum` becomes negative, reset it.
* Update `max_sum` before resetting `current_sum`.

Pattern learned:
Kadane’s Algorithm / Running Sum

Time Complexity: `O(n)`
Space Complexity: `O(1)`

---

## Problem 2: Remove Element

In **Remove Element**, I removed all values equal to `val` from the list.

My approach was to create a new list containing only the values that are not equal to `val`. Then I used:

```python
nums[:] = lst
```

This modifies the original `nums` list in-place. I also returned:

```python
len(nums)
```

because LeetCode asks for the new length after removing the target value.

Main lessons:

* Keep only the values that are not equal to `val`.
* `nums[:] = lst` modifies the original list.
* Returning the new length is required.
* This problem is similar to Move Zeroes because it changes the original list.

Pattern learned:
Array filtering + in-place update

Time Complexity: `O(n)`
Space Complexity: `O(n)` for my current version

---

## Problem 3: Remove Duplicates from Sorted Array

In **Remove Duplicates from Sorted Array**, I learned the two-pointer overwrite pattern.

At first, I used a list to store unique values. That worked logically, but then I understood the better in-place version.

The important idea is:

```text
i = scanning pointer
k = position where the next unique value should go
```

Because the array is sorted, duplicate values stay next to each other. So I can compare the current value with the previous unique value. If it is different, I place it at index `k` and move `k` forward.

Main lessons:

* The array is sorted, so duplicates are next to each other.
* `i` scans through the list.
* `k` tracks where the next unique number should be placed.
* This is an in-place overwrite pattern.
* The return value is `k`, the number of unique values.

Pattern learned:
Two Pointers / Overwrite Position

Time Complexity: `O(n)`
Space Complexity: `O(1)` for the two-pointer version

---

## Project improvement

Today I added these problems to my DSA Tracker:

```text
Maximum Subarray
Remove Element
Remove Duplicates from Sorted Array
```

This brought my total tracked solved problems to **10**.

## Reflection

Today was important because I started seeing repeated patterns across array problems. I understood that some problems need a running sum, some need in-place replacement, and some need a pointer to track the next valid position. I also learned that my first solution can be logically correct but not always optimal. The goal is to first understand the problem clearly, then improve the solution step by step.
