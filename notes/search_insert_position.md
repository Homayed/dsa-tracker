# Search Insert Position Review

Pattern:
Binary Search

Main idea:
The array is sorted.
Find the target index if it exists.
If not, return the index where it should be inserted.

Pointer meaning:
left = start of search area
right = end of search area
mid = middle index

Steps:
1. Set left = 0 and right = len(nums) - 1.
2. Find mid.
3. If nums[mid] == target, return mid.
4. If nums[mid] < target, search right side.
5. If nums[mid] > target, search left side.
6. If target is not found, return left.

Time Complexity: O(log n)
Space Complexity: O(1)

Mistake to remember:
When the loop ends, left is the correct insert position.

# Search Insert Position Review

Pattern:
Binary Search

Main idea:
Use binary search to find the target.
If target is not found, return left because left becomes the correct insert position.

Key rules:
If target > nums[middle], move left to middle + 1.
If target < nums[middle], move right to middle - 1.

Mistake to remember:
Do not use left = middle or right = middle because it can get stuck.
Use middle + 1 or middle - 1.

Time Complexity: O(log n)
Space Complexity: O(1)