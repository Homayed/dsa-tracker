
# CU Boulder Module 1 Final Note

## Module 1: Algorithms, Searching, Sorting, and Asymptotic Notation

This module introduced the foundation of algorithm thinking. I studied how algorithms are designed, how to prove they are correct, how to analyze their running time, and how sorting/searching algorithms work.

The main topics I covered were:

```text
1. Insertion Sort
2. Binary Search
3. Merge Sort
4. Asymptotic Notation: Big-O, Omega, Theta
5. Recursive Binary Search
6. Integer Cube Root using Binary Search
7. Two-Way Merge
8. K-Way Merge
9. Algorithm correctness using invariants
10. Running time analysis
```

---

# 1. Insertion Sort

## Main Idea

Insertion sort builds a sorted part of the array from left to right.

The idea is similar to sorting playing cards in your hand.

```text
Take the current element.
Compare it with the sorted part on the left.
Shift bigger values to the right.
Insert the current element into the correct position.
```

Example:

```text
[5, 2, 4, 6, 1, 3]
```

At first:

```text
[5] is sorted.
```

Then `2` is inserted before `5`:

```text
[2, 5]
```

Then `4` is inserted between `2` and `5`:

```text
[2, 4, 5]
```

This continues until the whole array becomes sorted.

---

## CLRS Pseudocode Idea

CLRS uses 1-based indexing:

```text
INSERTION-SORT(A)

for j = 2 to A.length
    key = A[j]
    i = j - 1

    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1

    A[i + 1] = key
```

Python uses 0-based indexing, so the loop starts from index `1`.

---

## Important Lines

```python
arr[i + 1] = arr[i]
```

This shifts a bigger value one step to the right.

```python
arr[i + 1] = key
```

This inserts the key into the correct position.

The value is not lost because it is stored in `key`.

---

## Insertion Sort Python Practice

I coded insertion sort in:

```text
practice/insertion_sort.py
```

Main logic:

```python
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1

        arr[i + 1] = key

    return arr
```

---

## Insertion Sort Complexity

Best case:

```text
O(n)
```

This happens when the array is already sorted.

Worst case:

```text
O(n²)
```

This happens when the array is reverse sorted.

Average case:

```text
O(n²)
```

Space complexity:

```text
O(1)
```

Insertion sort sorts in-place.

---

## Main Lesson

```text
Insertion sort is simple and useful for small or nearly sorted arrays.
But for large unsorted arrays, it can be slow because the worst case is O(n²).
```

---

# 2. Binary Search

## Main Idea

Binary search works on a sorted array.

Instead of checking every element one by one, binary search checks the middle element.

If the target is bigger than the middle value, search the right half.

If the target is smaller than the middle value, search the left half.

Each step cuts the search space in half.

---

## Binary Search Python Practice

I coded binary search in:

```text
practice/binary_search.py
```

Main logic:

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if target > arr[mid]:
            left = mid + 1

        if target < arr[mid]:
            right = mid - 1

    return -1
```

---

## Important Lesson

```text
Do not move mid directly.
Move left or right.
Then recalculate mid.
```

If target is bigger:

```python
left = mid + 1
```

If target is smaller:

```python
right = mid - 1
```

---

## Binary Search Complexity

Time complexity:

```text
O(log n)
```

Space complexity:

```text
O(1)
```

The reason it is `O(log n)` is because the search space is divided by 2 each time.

Example:

```text
16 → 8 → 4 → 2 → 1
```

---

## Connection to LeetCode

Binary search connects to:

```text
Search Insert Position
```

In Search Insert Position, if the target is not found, return `left`.

In normal binary search, if the target is not found, return `-1`.

---

# 3. Merge Sort

## Main Idea

Merge sort is a divide-and-conquer sorting algorithm.

It has three steps:

```text
1. Divide
2. Conquer
3. Combine
```

Meaning:

```text
Divide the array into halves.
Recursively sort both halves.
Merge the sorted halves.
```

---

## Base Case

The base case is:

```text
If the array has 0 or 1 element, it is already sorted.
```

In code:

```python
if len(arr) <= 1:
    return arr
```

---

## Merge Step

Before coding full merge sort, I first practiced merging two sorted lists.

Example:

```text
left = [2, 4, 6]
right = [1, 3, 5]
```

Merged result:

```text
[1, 2, 3, 4, 5, 6]
```

I coded this in:

```text
practice/merge_two_sorted_lists.py
```

Main idea:

```text
i tracks the left list.
j tracks the right list.
Compare left[i] and right[j].
Append the smaller one.
Move that pointer forward.
After one list finishes, add the remaining values.
```

---

## Merge Sort Python Practice

I coded merge sort in:

```text
practice/merge_sort.py
```

Main logic:

```python
def merge(left, right):
    lst = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1

    lst.extend(left[i:])
    lst.extend(right[j:])

    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    arr_left = arr[:mid]
    arr_right = arr[mid:]

    sorted_left = merge_sort(arr_left)
    sorted_right = merge_sort(arr_right)

    return merge(sorted_left, sorted_right)
```

---

## Important Lesson

Merge sort becomes easier when I separate it into two parts:

```text
1. merge two sorted lists
2. recursively split and merge
```

The hardest part was understanding that recursive calls return sorted lists:

```python
sorted_left = merge_sort(arr_left)
sorted_right = merge_sort(arr_right)
```

Then:

```python
return merge(sorted_left, sorted_right)
```

---

## Merge Sort Complexity

Time complexity:

```text
O(n log n)
```

Why?

```text
The array is split into halves → log n levels.
At each level, merging processes all n elements.
Total = O(n log n)
```

Space complexity:

```text
O(n)
```

because merge sort creates extra lists while merging.

---

# 4. Asymptotic Notation

Asymptotic notation describes how an algorithm grows as input size increases.

The three main notations are:

```text
Big-O
Omega
Theta
```

---

## Big-O

Big-O is an upper bound.

It means:

```text
The algorithm does not grow faster than this rate.
```

Example:

```text
3n² = O(n²)
3n² = O(n³)
```

But `O(n³)` is a loose upper bound for `3n²`.

---

## Omega

Omega is a lower bound.

It means:

```text
The algorithm grows at least this fast.
```

Example:

```text
3n² = Ω(n²)
3n² = Ω(n)
```

But `Ω(n)` is a weak lower bound.

---

## Theta

Theta is a tight bound.

It means:

```text
The algorithm grows exactly at this rate, ignoring constants and lower-order terms.
```

Example:

```text
3n² = Θ(n²)
```

---

## Big-O vs Omega vs Theta

```text
O(g(n)) = upper bound
Ω(g(n)) = lower bound
Θ(g(n)) = tight bound
```

Example:

```text
f(n) = 3n²
g(n) = n³
```

Then:

```text
f(n) = O(g(n))
f(n) is not Ω(g(n))
f(n) is not Θ(g(n))
```

Because `n²` grows slower than `n³`.

---

## Growth Order

From slower to faster:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2ⁿ)
O(n!)
```

Important rule:

```text
Exponential beats polynomial.
2ⁿ grows faster than n².
```

Example:

```text
1.5 × 2ⁿ + 1.2 × n² = Θ(2ⁿ)
```

because `2ⁿ` dominates.

---

## Main Rule

```text
Ignore constants.
Ignore lower-order terms.
Keep the fastest-growing term.
```

Examples:

```text
3n + 1 = Θ(n)
5n² + 2n + 10 = Θ(n²)
1.5 × 2ⁿ + 1.2 × n² = Θ(2ⁿ)
```

---

# 5. Algorithm Correctness and Invariants

An invariant is a condition that stays true during an algorithm.

In recursive search problems, the invariant helps prove the answer remains inside the current search region.

---

## Example: Crossover Index Problem

The problem was to find an index where one relationship changes.

The helper maintained:

```text
left = safe side
right = crossed side
```

For the crossover problem:

```text
x[left] >= y[left]
x[right] < y[right]
```

The answer must be between `left` and `right`.

---

## Recursive Binary Search Pattern

The logic was:

```text
If left and right are adjacent:
    return left

Find mid.

If mid is still on the safe side:
    search mid to right

If mid is already crossed:
    search left to mid
```

This is recursive binary search, but instead of searching for a target number, it searches for where a condition changes.

---

## What I Learned

```text
Assertions help check assumptions.
Invariants help keep the search region valid.
Recursive binary search reduces the problem size each call.
```

---

# 6. Integer Cube Root

## Problem

Find integer cube root of `n`.

The answer is the smallest integer `i` such that:

```text
i³ <= n
and
(i + 1)³ > n
```

Example:

```text
integer cube root of 100 = 4
because 4³ <= 100 and 5³ > 100
```

---

## Helper Invariant

The helper maintained:

```text
left³ < n
right³ > n
```

So:

```text
left = too small / safe side
right = too big / crossed side
```

---

## Recursive Logic

```text
If right and left are adjacent:
    return left

Find mid.

If mid³ == n:
    return mid

If mid³ < n:
    mid is too small, so search mid to right

If mid³ > n:
    mid is too big, so search left to mid
```

---

## What I Learned

This problem helped me understand recursive binary search better.

The main lesson was:

```text
When mid is safe, move left to mid.
When mid is too big, move right to mid.
Always preserve the invariant.
```

---

# 7. Two-Way Merge

## Main Idea

Two-way merge combines two sorted lists into one sorted list.

Example:

```text
lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
```

Merged result:

```text
[1, 2, 3, 4, 5, 6]
```

---

## Pointers

```text
i = pointer for lst1
j = pointer for lst2
result = merged list
```

Compare:

```text
lst1[i] and lst2[j]
```

Append the smaller value.

When one list finishes, append the remaining values from the other list.

---

## Complexity

If list sizes are `m` and `n`:

```text
Time complexity = Θ(m + n)
```

because every element is processed once.

---

# 8. K-Way Merge / Multiway Merge

## Problem

Merge `k` sorted lists into one sorted list.

There were two strategies.

---

## Strategy 1: Merge One by One

Start with:

```text
mergedList = lists[0]
```

Then repeatedly merge:

```text
mergedList with lists[1]
mergedList with lists[2]
mergedList with lists[3]
...
```

If each list has size `n`, the costs are:

```text
2n + 3n + 4n + ... + kn
```

So the total is:

```text
Θ(nk²)
```

This is slower.

---

## Strategy 2: Balanced Pairwise Merge

Merge consecutive pairs:

```text
lists[0] with lists[1]
lists[2] with lists[3]
lists[4] with lists[5]
...
```

Then repeat until one list remains.

This works like merge sort.

At each level, all elements are processed once.

Total elements:

```text
nk
```

Number of levels:

```text
log k
```

So total running time:

```text
Θ(nk log k)
```

This is faster than one-by-one merging.

---

## What I Learned

```text
Balanced merging is better than merging one list at a time.
This is the same divide-and-conquer idea used in merge sort.
```

---

# 9. Module 1 Assignment

I completed the Module 1 assignment/problem set and received:

```text
100/100
```

Problems completed:

```text
1. Find Crossover Indices
2. Integer Cube Root
3. K-Way Merge / Multiway Merge
```

---

## Problem 1: Find Crossover Indices

Main pattern:

```text
Recursive Binary Search
```

Main idea:

```text
Use left and right boundaries.
Maintain an invariant.
Shrink the search region recursively.
```

I learned how to use assertions to protect the recursive helper.

---

## Problem 2: Integer Cube Root

Main pattern:

```text
Recursive Binary Search
```

Main idea:

```text
Use cube(mid) to decide whether to search left or right.
```

I learned that recursive binary search can be used for numeric answer search, not just array search.

---

## Problem 3: K-Way Merge

Main pattern:

```text
Divide and Conquer / Repeated Merge
```

Main idea:

```text
Merge pairs of sorted lists repeatedly until one sorted list remains.
```

I learned that balanced merging improves the running time from:

```text
Θ(nk²)
```

to:

```text
Θ(nk log k)
```

---

# 10. Connection to My LeetCode Progress

Module 1 connects to my solved LeetCode problems.

---

## HashMap Problems

```text
Contains Duplicate
Valid Anagram
Two Sum
Contains Duplicate II
```

These helped me understand `O(n)` one-pass algorithms.

---

## Binary Search

```text
Search Insert Position
```

This connected directly to the binary search lecture and recursive search assignment problems.

---

## Sorting

```text
Merge Sorted Array
```

This connected to sorting and merge sort.

---

## Prefix/Suffix

```text
Product of Array Except Self
```

This showed how brute force `O(n²)` can be improved to `O(n)`.

---

## Running Sum

```text
Maximum Subarray
```

This connected to the idea of tracking only what is necessary instead of storing everything.

---

# 11. Key Mistakes I Fixed During This Module

## Binary Search Mistake

I first tried to move `mid` directly.

Correct lesson:

```text
Move left or right, then recalculate mid.
```

---

## Right Boundary Mistake

I sometimes wrote:

```python
right = len(arr)
```

Correct:

```python
right = len(arr) - 1
```

because list indexes start at 0.

---

## Recursive Return Mistake

In merge sort, I first called recursive functions but did not store their returned values.

Correct:

```python
sorted_left = merge_sort(arr_left)
sorted_right = merge_sort(arr_right)
```

---

## Merge Sort Split Mistake

I first wrote:

```python
arr[:mid-1]
```

Correct:

```python
arr[:mid]
```

because `arr[:mid-1]` skips an element.

---

## Assignment Invariant Mistake

I had to learn that if `mid` is on the safe side, it should become the new safe boundary.

Example:

```text
safe mid → search mid to right
crossed mid → search left to mid
```

---

# 12. Final Module 1 Takeaways

The biggest lessons from Module 1:

```text
1. Algorithms can be proven correct using invariants.
2. Binary search is not only for finding numbers; it can find transition points.
3. Recursion works by solving a smaller version of the same problem.
4. Merge sort is divide, conquer, and combine.
5. Big-O, Omega, and Theta describe growth rates.
6. Balanced merging is faster than sequential merging.
7. Brute force is useful for understanding, but analysis helps find better solutions.
```

---

# Final Reflection

Module 1 helped me connect theory with coding.

Before this module, I understood some algorithms only from LeetCode practice. Now I understand them more deeply through CLRS and CU Boulder.

I practiced:

```text
Insertion sort
Binary search
Recursive binary search
Merge sort
Two-way merge
K-way merge
Asymptotic notation
Algorithm correctness
Invariants
```

I also completed the Module 1 assignment with:

```text
100/100
```

This is an important checkpoint in my CU Boulder MS-CS preparation.

My next step is to continue the next module/topic while keeping LeetCode review active.
