# Sorting Basics Mini Note

Sorting means arranging data in order, usually ascending or descending.

In Python, `sorted()` creates a new sorted list.

Example:
nums = [3, 1, 2]
sorted(nums) gives [1, 2, 3]

`list.sort()` modifies the original list in-place.

Sorting is important because sorted data makes searching easier.

Python sorting usually takes O(n log n).

Connection to my solved problem:
In Merge Sorted Array, I used:

nums1[:] = sorted(nums1[:m] + nums2)

This means:
1. Take the real values from nums1 using nums1[:m]
2. Add nums2
3. Sort the merged list
4. Update nums1 in-place using nums1[:]