

# Day 10 Progress

Today I solved **Contains Duplicate II** and **Product of Array Except Self**. This was an important day because I practiced two stronger patterns: **hash map index-distance checking** and **prefix/suffix product**.

## Problem 1: Contains Duplicate II

In **Contains Duplicate II**, I extended my understanding of the original Contains Duplicate problem.

The original Contains Duplicate only asks whether a duplicate exists. But Contains Duplicate II adds one more condition: the duplicate values must appear within distance `k`.

At first, I tried to compare indexes manually using `i` and `j`, but that became confusing. Then I understood that the better approach is to store the latest index of each number in a dictionary.

Main idea:

```text
number → latest index
```

When I see the same number again, I check the distance:

```text
current index - previous index <= k
```

If the distance is less than or equal to `k`, then I return `True`.

Main lessons:

* This problem is not only about duplicates.
* It also checks how close the duplicate indexes are.
* A dictionary can store the latest index of each number.
* `seen[num]` gives the previous index of that number.
* `i - seen[num]` gives the distance between duplicate values.
* After checking, I update `seen[num]` to the latest index.

Pattern learned:
Hash Map / Index Distance Checking

Time Complexity: `O(n)`
Space Complexity: `O(n)`

---

## Problem 2: Product of Array Except Self

In **Product of Array Except Self**, I first understood the brute force approach.

For each index, I tried to multiply every other number except the current one. This worked logically, but it caused Time Limit Exceeded because it used nested loops.

Brute force idea:

```text
For every index i:
    multiply every nums[j] where i != j
```

Time complexity of brute force:

```text
O(n²)
```

Then I learned the optimized pattern:

```text
Prefix Product + Suffix Product
```

The main idea is:

```text
answer[i] = product before i × product after i
```

## Prefix meaning

Prefix means everything before the current index.

Example:

```text
nums = [1, 2, 3, 4]

prefix products:
index 0 → before 1 = 1
index 1 → before 2 = 1
index 2 → before 3 = 1 × 2 = 2
index 3 → before 4 = 1 × 2 × 3 = 6
```

So after the prefix pass:

```text
answer = [1, 1, 2, 6]
```

## Suffix meaning

Suffix means everything after the current index.

Example:

```text
nums = [1, 2, 3, 4]

suffix products:
index 3 → after 4 = 1
index 2 → after 3 = 4
index 1 → after 2 = 3 × 4 = 12
index 0 → after 1 = 2 × 3 × 4 = 24
```

The suffix loop goes from right to left using:

```python
range(len(nums) - 1, -1, -1)
```

This means:

```text
Start from the last index.
Move backward by 1.
Stop after reaching index 0.
```

For `[1, 2, 3, 4]`, the loop indexes are:

```text
3, 2, 1, 0
```

## Why answer starts with 1

I learned why we use:

```python
answer = [1] * len(nums)
```

This creates an answer list with the same length as `nums`.

Example:

```text
nums = [1, 2, 3, 4]
answer = [1, 1, 1, 1]
```

We use `1` because multiplication starts safely from `1`.

If we used `0`, every product would become `0`.

Main lessons:

* Brute force works logically but is too slow.
* Nested loops cause `O(n²)` time.
* Prefix means product before the current index.
* Suffix means product after the current index.
* `answer[i]` stores prefix first.
* Then suffix multiplies into `answer[i]`.
* `range(len(nums)-1, -1, -1)` loops from right to left.
* `answer = [1] * len(nums)` creates the output container.
* Product of Array Except Self can be solved without division.

Pattern learned:
Prefix / Suffix Product

Time Complexity: `O(n)`
Space Complexity: `O(1)` extra space, excluding the output array

---

## Project improvement

Today I should add these problems to my DSA Tracker:

```text
Contains Duplicate II
Product of Array Except Self
```

Tracker details:

```text
Contains Duplicate II
Pattern: Hash Map / Index Distance Checking
Time Complexity: O(n)
Space Complexity: O(n)

Product of Array Except Self
Pattern: Prefix / Suffix Product
Time Complexity: O(n)
Space Complexity: O(1) extra space, excluding output array
```

## Reflection

Today I learned that brute force is useful for understanding a problem, but it is not always efficient enough. In Product of Array Except Self, brute force helped me understand the meaning of “except self,” but the optimized solution required a new way of thinking: using products from the left side and right side.

I also improved my understanding of hash maps with indexes in Contains Duplicate II. I learned that dictionaries can store not only counts, but also positions. This helped me understand how to solve problems that involve distance between duplicate values.

Today was important because I moved from basic Easy patterns into more serious interview patterns like prefix/suffix and index-distance checking.
