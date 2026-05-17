
# Weekly Review — First 13 LeetCode Problems

Today I reviewed my first **13 LeetCode problems**. The goal was not just to memorize code, but to remember the **pattern**, **data structure**, **time complexity**, **space complexity**, **main idea**, and **mistakes I made**.

---

## 1. Contains Duplicate

Problem: Contains Duplicate
Pattern: Seen-before checking
Data structure: Dictionary / HashSet
Time complexity: O(n)
Space complexity: O(n)
Main idea: Store each number when I first see it. If the same number appears again, return `True` immediately.
Main mistake I made: I first tried nested loops and also confused whether I should store index or value.
Can I solve it again without looking? Yes.

---

## 2. Valid Anagram

Problem: Valid Anagram
Pattern: Character frequency counting
Data structure: Dictionary / HashMap
Time complexity: O(n)
Space complexity: O(n)
Main idea: Count characters in `s`, subtract characters from `t`, then check if all counts become zero.
Main mistake I made: I first tried returning `True` too early when one character count became zero. I learned that all counts must be checked before returning `True`.
Can I solve it again without looking? Yes.

---

## 3. Two Sum

Problem: Two Sum
Pattern: Complement lookup
Data structure: Dictionary / HashMap
Time complexity: O(n)
Space complexity: O(n)
Main idea: For each number, calculate `needed = target - num`. If `needed` already exists in the dictionary, return the saved index and the current index.
Main mistake I made: I first stored the current number before checking the needed number, and I also confused number-to-index with index-to-number.
Can I solve it again without looking? Yes.

---

## 4. Best Time to Buy and Sell Stock

Problem: Best Time to Buy and Sell Stock
Pattern: One-pass tracking
Data structure: Variables
Time complexity: O(n)
Space complexity: O(1)
Main idea: Track the lowest price so far and calculate the profit if selling today. Update `max_profit` whenever a better profit is found.
Main mistake I made: I first tried nested loops and stored all possible profits, which caused time and memory issues.
Can I solve it again without looking? Yes.

---

## 5. Valid Palindrome

Problem: Valid Palindrome
Pattern: Two Pointers
Data structure: Cleaned list / string
Time complexity: O(n)
Space complexity: O(n)
Main idea: Clean the string by keeping only alphanumeric characters, convert everything to lowercase, then compare left and right characters while moving inward.
Main mistake I made: I first compared characters incorrectly and forgot that uppercase/lowercase should be treated the same. I also learned that `isalnum()` removes spaces, commas, and symbols.
Can I solve it again without looking? Yes.

---

## 6. Move Zeroes

Problem: Move Zeroes
Pattern: In-place array modification
Data structure: Lists
Time complexity: O(n)
Space complexity: O(n) for my current version
Main idea: Store non-zero values in one list and zeroes in another list, then combine them and update the original list using `nums[:]`.
Main mistake I made: I first tried returning a new list, but LeetCode wanted the original `nums` list modified in-place.
Can I solve it again without looking? Yes.

---

## 7. Merge Sorted Array

Problem: Merge Sorted Array
Pattern: Array slicing + in-place update
Data structure: List
Time complexity: O((m+n) log(m+n))
Space complexity: O(m+n)
Main idea: Use `nums1[:m]` to keep only the real values from `nums1`, merge with `nums2`, sort the result, then update `nums1` using `nums1[:]`.
Main mistake I made: I first tried to remove zeroes manually and got confused with `pop()`. I learned that the zeroes are placeholders and `m` tells how many real values are inside `nums1`.
Can I solve it again without looking? Yes.

---

## 8. Maximum Subarray

Problem: Maximum Subarray
Pattern: Kadane’s Algorithm / Running Sum
Data structure: Variables
Time complexity: O(n)
Space complexity: O(1)
Main idea: For each number, decide whether to continue the current subarray or restart from the current number, while tracking the best sum found so far.
Main mistake I made: I first initialized `max_sum` as `0`, which fails for all-negative arrays. I learned to use `max_sum = nums[0]`.
Can I solve it again without looking? Yes.

---

## 9. Remove Element

Problem: Remove Element
Pattern: Array filtering + in-place update
Data structure: List
Time complexity: O(n)
Space complexity: O(n) for my current version
Main idea: Keep only the numbers that are not equal to `val`, replace the original `nums` using `nums[:]`, and return the new length.
Main mistake I made: I needed to remember that LeetCode asks for the new length, not just the modified list.
Can I solve it again without looking? Yes.

---

## 10. Remove Duplicates from Sorted Array

Problem: Remove Duplicates from Sorted Array
Pattern: Two Pointers / Overwrite Position
Data structure: Variables
Time complexity: O(n) for the two-pointer version
Space complexity: O(1) for the two-pointer version
Main idea: Because the array is sorted, duplicates stay next to each other. Use `i` to scan the array and `k` to track where the next unique value should be placed.
Main mistake I made: I first used a separate list, which worked logically but was not the best interview-style solution. I also learned that the two-pointer version is better because it modifies in-place with O(1) extra space.
Can I solve it again without looking? Mostly yes, but I should review the two-pointer version again.

---

## 11. Search Insert Position

Problem: Search Insert Position
Pattern: Binary Search
Data structure: Sorted Array
Time complexity: O(log n)
Space complexity: O(1)
Main idea: Use `left`, `right`, and `mid` to search a sorted array. If the target is not found, return `left` because it becomes the correct insert position.
Main mistake I made: I tried to move `mid` directly. I learned that I should move `left` or `right`, then recalculate `mid`.
Can I solve it again without looking? Yes, but I should keep practicing binary search.

---

## 12. Contains Duplicate II

Problem: Contains Duplicate II
Pattern: HashMap / Index Distance Checking
Data structure: Dictionary
Time complexity: O(n)
Space complexity: O(n)
Main idea: Store each number’s latest index. If the same number appears again and the distance between the current index and previous index is less than or equal to `k`, return `True`.
Main mistake I made: I first tried to compare indexes manually with `i` and `j`. I learned that storing the latest index in a dictionary is much cleaner.
Can I solve it again without looking? Yes.

---

## 13. Product of Array Except Self

Problem: Product of Array Except Self
Pattern: Prefix / Suffix Product
Data structure: List
Time complexity: O(n)
Space complexity: O(1) extra space, excluding output array
Main idea: First store the product of everything before each index, then multiply by the product of everything after each index using a reverse loop.
Main mistake I made: I first solved it with brute force nested loops, which caused Time Limit Exceeded. I also got confused about why `answer = [1] * len(nums)` is needed and why the suffix loop goes from right to left.
Can I solve it again without looking? Yes, but this is still one of the newest patterns, so I should review it again.

---

# Patterns Reviewed

## HashMap / Set

Problems:

* Contains Duplicate
* Valid Anagram
* Two Sum
* Contains Duplicate II

Main idea:
Use a dictionary or set when I need to remember something I have already seen, count frequency, or store an index.

---

## Two Pointers

Problems:

* Valid Palindrome
* Remove Duplicates from Sorted Array

Main idea:
Use two indexes when comparing from both ends or when tracking where the next valid value should go.

---

## In-place Array Modification

Problems:

* Move Zeroes
* Remove Element
* Merge Sorted Array

Main idea:
When LeetCode says modify in-place, use `nums[:] = new_list` or overwrite values directly instead of returning a new list.

---

## One-pass Tracking

Problems:

* Best Time to Buy and Sell Stock
* Maximum Subarray

Main idea:
Sometimes I do not need to store everything. I only need variables like `min_price`, `max_profit`, `current_sum`, or `max_sum`.

---

## Binary Search

Problem:

* Search Insert Position

Main idea:
Use `left`, `right`, and `mid`. Compare target with `nums[mid]`, move the boundaries, and return `left` if the target is not found.

---

## Prefix / Suffix

Problem:

* Product of Array Except Self

Main idea:
For each index, use product before it and product after it.

---

# Overall Reflection

This review helped me see that I am not just solving random problems anymore. I am starting to recognize patterns.

The biggest lessons from these 13 problems are:

* Read the return requirement carefully.
* Know whether the problem wants a boolean, index, length, list, or in-place modification.
* Brute force helps me understand the problem, but I should then look for a better pattern.
* Dictionaries can store counts, indexes, or seen values.
* `nums[:]` modifies the original list.
* Binary search moves `left` and `right`, not `mid`.
* Prefix means product before me, suffix means product after me.
* Pattern recognition is the real DSA skill.

Current solved problems: 13
Current strongest patterns: HashMap, in-place arrays, basic binary search
Current weakest/newest pattern: Prefix / Suffix Product
Next focus: Review patterns, continue CU Boulder Module 1, and then move toward new patterns like Sliding Window and Stack.
