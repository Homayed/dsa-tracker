# Day 12 — Top K Frequent Elements, Valid Parentheses, and Longest Consecutive Sequence Review

## Today's Focus

Today was a review, cleanup, and progress day.

I studied before work and also continued reviewing later. The main goal was to clean up my Day 22 roadmap and strengthen important DSA patterns before moving forward.

Main topics covered:

- Top K Frequent Elements
- Valid Parentheses
- Longest Consecutive Sequence concept
- Stack basics
- Hash Map
- Min Heap
- Bucket Sort
- Hash Set

---

# 0. Workday Progress Summary

Today I studied both before work and after work.

Before work, I focused on cleaning up my Day 22 roadmap and reviewing important DSA problems.

## Before Work

I worked on:

- Reviewing Top K Frequent Elements
- Understanding the sorting version
- Understanding `key=lambda x: dic[x]`
- Reviewing the heap version
- Reviewing the bucket sort idea
- Adding Top K Frequent Elements to the tracker
- Reviewing stack basics
- Solving Valid Parentheses step by step
- Understanding the dictionary version of Valid Parentheses
- Understanding what `dic[c]` means
- Dry running Valid Parentheses with the example `s = "([])"`

## After Work / Later Review

I continued with:

- Reviewing Longest Consecutive Sequence concept
- Understanding the Hash Set pattern
- Understanding the key line `if num - 1 not in num_set`
- Planning to mark Longest Consecutive Sequence for weekend practice
- Preparing the Day 22 cleanup list
- Combining all notes into `day_12.md`

## Main Progress Today

Today was not only a coding day. It was also a cleanup and understanding day.

I improved my understanding of:

- Hash Map frequency counting
- Sorting dictionary keys by value
- Min Heap for Top K problems
- Bucket Sort concept for frequency problems
- Stack pattern for Valid Parentheses
- Dictionary matching pairs
- Hash Set concept for Longest Consecutive Sequence

## Current Confidence

```text
Top K Frequent Sorting Version: Good
Top K Frequent Heap Version: Good
Top K Frequent Bucket Sort Version: Needs weekend review
Valid Parentheses Basic Version: Good
Valid Parentheses Dictionary Version: Good
Longest Consecutive Sequence: Concept reviewed, needs coding practice
```

---

# 1. Top K Frequent Elements

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

Example:

```python
nums = [1,1,1,2,2,3]
k = 2
```

Frequency:

```text
1 -> 3 times
2 -> 2 times
3 -> 1 time
```

Answer:

```python
[1, 2]
```

Order does not matter.

---

## Topic

Arrays & Hashing

## Patterns

- Hash Map + Sorting
- Hash Map + Min Heap
- Hash Map + Bucket Sort

---

## Version 1: Hash Map + Sorting

### Idea

First count the frequency of each number using a dictionary.

Then sort the dictionary keys based on their frequency.

### Code

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        lst = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)

        return lst[:k]
```

### Key Line

```python
sorted(dic.keys(), key=lambda x: dic[x], reverse=True)
```

This means:

```text
Sort the dictionary keys based on their values/frequencies from highest to lowest.
```

Example:

```python
dic = {
    1: 3,
    2: 2,
    3: 1
}
```

Then:

```python
dic.keys()
```

gives:

```python
[1, 2, 3]
```

And:

```python
key=lambda x: dic[x]
```

means:

```text
For each key x, sort by dic[x].
```

So:

```text
1 is sorted by dic[1] = 3
2 is sorted by dic[2] = 2
3 is sorted by dic[3] = 1
```

Because `reverse=True`, the highest frequency comes first.

### What `lambda` Means

```python
lambda x: dic[x]
```

is a short one-line function.

It is similar to:

```python
def get_frequency(x):
    return dic[x]
```

So this line:

```python
sorted(dic.keys(), key=lambda x: dic[x], reverse=True)
```

means:

```text
Sort each key using its frequency as the sorting value.
```

### Complexity

```text
Time: O(n + m log m)
Space: O(m)
```

Where:

```text
n = total numbers in nums
m = unique numbers in nums
```

Reason:

```text
O(n) for counting frequency
O(m log m) for sorting unique numbers
```

---

## Version 2: Hash Map + Min Heap

### Idea

Use a dictionary to count frequency.

Then use a min heap of size `k`.

The heap stores:

```python
(freq, num)
```

If heap size becomes bigger than `k`, remove the smallest frequency.

That way, the heap keeps only the top `k` frequent numbers.

### Code

```python
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        heap = []

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for num in dic:
            freq = dic[num]
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for freq, num in heap:
            result.append(num)

        return result
```

### Important Heap Idea

Python heap is a min heap.

That means the smallest item stays at the top.

For Top K Frequent, we push:

```python
(freq, num)
```

So the smallest frequency gets removed first.

### Example

```python
nums = [1,1,1,2,2,3]
k = 2
```

Frequency:

```python
{
    1: 3,
    2: 2,
    3: 1
}
```

Heap pushes:

```text
(3, 1)
(2, 2)
(1, 3)
```

When heap size becomes bigger than `k`, remove the smallest:

```text
(1, 3)
```

Final heap contains:

```text
(3, 1), (2, 2)
```

Answer:

```python
[1, 2]
```

or:

```python
[2, 1]
```

Both are accepted because order does not matter.

### Complexity

```text
Time: O(n + m log k)
Space: O(m)
```

Where:

```text
n = total numbers
m = unique numbers
k = number of top frequent elements needed
```

In interviews, this is commonly written as:

```text
Time: O(n log k)
Space: O(n)
```

### Interview Explanation

```text
I count the frequency of each number using a hash map.

Then I use a min heap of size k.

For every unique number, I push (frequency, number) into the heap.

If the heap size becomes greater than k, I pop the smallest frequency.

At the end, the heap contains the k most frequent elements.
```

---

## Version 3: Hash Map + Bucket Sort

### Idea

Use a dictionary to count frequency.

Then create buckets where the index represents frequency.

Example:

```python
bucket[3] = numbers that appear 3 times
bucket[2] = numbers that appear 2 times
bucket[1] = numbers that appear 1 time
```

### Code

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num in dic:
            freq = dic[num]
            bucket[freq].append(num)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
```

### Key Line

```python
bucket[freq].append(num)
```

This means:

```text
Put the number inside the bucket that represents its frequency.
```

Example:

```python
nums = [1,1,1,2,2,3]
```

Frequency:

```text
1 -> 3
2 -> 2
3 -> 1
```

Bucket:

```text
bucket[3] = [1]
bucket[2] = [2]
bucket[1] = [3]
```

Then scan from the back:

```text
highest frequency -> lowest frequency
```

### Why `len(nums) + 1`?

```python
bucket = [[] for _ in range(len(nums) + 1)]
```

The maximum frequency of any number can be `len(nums)`.

Example:

```python
nums = [1,1,1,1]
```

Here, `1` appears 4 times.

So we need:

```python
bucket[4]
```

That is why the bucket size is:

```python
len(nums) + 1
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

### My Status

```text
Sorting version: understood
Heap version: reviewed and understood better
Bucket sort version: weaker, needs weekend review
```

---

# 2. Valid Parentheses

## Problem

Given a string containing brackets:

```text
( ) { } [ ]
```

Return `True` if every opening bracket is closed in the correct order.

Example:

```python
s = "([])"
```

Answer:

```python
True
```

Bad example:

```python
s = "(]"
```

Answer:

```python
False
```

---

## Topic

Stack

## Pattern

Stack + Matching Pairs

---

## Main Idea

Use a stack to remember the most recent opening bracket.

Rules:

```text
Opening bracket -> push into stack
Closing bracket -> check top of stack
If top matches -> pop
If top does not match -> return False
At the end -> stack must be empty
```

---

## Stack Basics

In Python, a list can be used as a stack.

```python
stack = []
```

Push:

```python
stack.append(x)
```

Pop:

```python
stack.pop()
```

Peek top:

```python
stack[-1]
```

Important:

```text
Do not pop or check stack[-1] if the stack is empty.
```

That is why we check:

```python
if not stack:
    return False
```

---

## First Version

```python
class Solution(object):
    def isValid(self, s):
        stack = []

        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)

            if p == "]":
                if not stack:
                    return False
                if stack[-1] != "[":
                    return False
                stack.pop()

            if p == "}":
                if not stack:
                    return False
                if stack[-1] != "{":
                    return False
                stack.pop()

            if p == ")":
                if not stack:
                    return False
                if stack[-1] != "(":
                    return False
                stack.pop()

        return len(stack) == 0
```

This version is longer, but it helped me understand the stack logic clearly.

---

## Dictionary Version

### Code

```python
class Solution(object):
    def isValid(self, s):
        dic = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)

            else:
                if not stack:
                    return False

                if stack[-1] != dic[c]:
                    return False

                stack.pop()

        return stack == []
```

---

## What `dic[c]` Means

Dictionary:

```python
dic = {
    ']': '[',
    '}': '{',
    ')': '('
}
```

Keys are closing brackets:

```text
]
}
)
```

Values are matching opening brackets:

```text
[
{
(
```

So:

```python
dic[']'] = '['
dic['}'] = '{'
dic[')'] = '('
```

Meaning:

```text
dic[c] gives the opening bracket that the closing bracket c needs.
```

Example:

```python
c = "]"
dic[c] = "["
```

So when the current character is `]`, the top of the stack must be `[`.

---

## Dry Run

Example:

```python
s = "([])"
```

Characters:

```text
(  [  ]  )
```

### Start

```python
stack = []
```

### Step 1

```python
c = "("
```

Opening bracket, so push:

```python
stack = ["("]
```

### Step 2

```python
c = "["
```

Opening bracket, so push:

```python
stack = ["(", "["]
```

### Step 3

```python
c = "]"
```

Closing bracket.

Check:

```python
dic[c]
```

means:

```python
dic["]"] = "["
```

Top of stack:

```python
stack[-1] = "["
```

Compare:

```python
stack[-1] != dic[c]
```

Becomes:

```python
"[" != "["
```

This is false, so it matches.

Now pop:

```python
stack.pop()
```

Stack becomes:

```python
["("]
```

### Step 4

```python
c = ")"
```

Closing bracket.

Check:

```python
dic[c]
```

means:

```python
dic[")"] = "("
```

Top of stack:

```python
stack[-1] = "("
```

Compare:

```python
"(" != "("
```

This is false, so it matches.

Now pop:

```python
stack.pop()
```

Stack becomes:

```python
[]
```

### End

```python
return stack == []
```

Stack is empty, so answer is:

```python
True
```

---

## Why We Return `stack == []`

If the stack is empty at the end, every opening bracket was matched.

Example:

```python
s = "()"
```

Stack becomes empty, so return:

```python
True
```

But:

```python
s = "(("
```

Stack is not empty at the end:

```python
["(", "("]
```

So:

```python
return stack == []
```

returns:

```python
False
```

---

## Complexity

```text
Time: O(n)
Space: O(n)
```

---

# 3. Longest Consecutive Sequence

## Problem

Given an unsorted array of numbers, return the length of the longest consecutive sequence.

Example:

```python
nums = [100, 4, 200, 1, 3, 2]
```

Longest sequence:

```text
1, 2, 3, 4
```

Answer:

```python
4
```

---

## Topic

Arrays & Hashing

## Pattern

Hash Set

---

## Main Idea

Use a set for fast lookup.

```python
num_set = set(nums)
```

The main trick is:

```python
if num - 1 not in num_set:
```

This means:

```text
Only start counting if num is the beginning of a sequence.
```

Example:

```python
nums = [100, 4, 200, 1, 3, 2]
```

Set:

```python
{100, 4, 200, 1, 3, 2}
```

Check:

```text
1 -> 0 not in set, so start counting
2 -> 1 is in set, so do not start
3 -> 2 is in set, so do not start
4 -> 3 is in set, so do not start
```

Start from `1`, then count:

```text
1 exists
2 exists
3 exists
4 exists
5 does not exist
```

Length:

```text
4
```

---

## Code To Review Later

```python
class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest
```

---

## Why We Use Set

We use a set because lookup is fast.

```python
num in num_set
```

is usually:

```text
O(1)
```

So we can quickly check whether the next number exists.

---

## My Status

```text
Concept reviewed
Not fully coded independently yet
Needs weekend practice
```

---

# 4. Day 22 Cleanup Status

## Completed

- Group Anagrams
- Two Sum II
- Top K Frequent Elements reviewed
- Top K Frequent Elements added to tracker
- Valid Parentheses solved
- Valid Parentheses dictionary version reviewed
- Valid Parentheses note prepared
- Module 1 Reflection completed

## Still Left

- Add Valid Parentheses to tracker
- Push latest tracker updates to GitHub
- Mark Longest Consecutive Sequence as weekend review
- Add total solved count feature
- Add Easy / Medium / Hard count feature
- Create `next_7_days_plan.md`

---

# 5. Key Lessons From Today

## Top K Frequent Elements

I learned three ways to solve it:

```text
1. Hash Map + Sorting
2. Hash Map + Min Heap
3. Hash Map + Bucket Sort
```

Main learning:

```text
Count frequency first.
Then find the top k most frequent elements.
```

---

## Valid Parentheses

Main learning:

```text
Stack is used when I need the most recent opening bracket.
```

Rules:

```text
Opening bracket -> push
Closing bracket -> compare with stack[-1]
Correct match -> pop
Wrong match -> return False
End -> stack must be empty
```

---

## Longest Consecutive Sequence

Main learning:

```text
Use a set and only start counting when num - 1 is not in the set.
```

This avoids counting the same sequence again and again.

---

# 6. Weekend Review Plan

## Review These

- Top K Frequent Elements bucket sort version
- Longest Consecutive Sequence
- Valid Parentheses dry run
- Stack basics
- Hash Set pattern

## Coding Practice

- Re-code Valid Parentheses without looking
- Re-code Top K Frequent heap version
- Try Longest Consecutive Sequence once
- Review bucket sort logic slowly

---

# Final Status

Today was a review, cleanup, and progress day.

I studied before work and later continued reviewing after work.

I am stronger in:

```text
Hash Map
Frequency counting
Sorting with lambda
Heap basics
Stack basics
Dictionary matching
Valid Parentheses dry run
Top K Frequent heap version
```

I still need more practice in:

```text
Bucket Sort
Hash Set sequence problems
Longest Consecutive Sequence
```

Next action:

```text
Add Valid Parentheses to tracker
Push tracker and notes to GitHub
Create next_7_days_plan.md
Add tracker count features
```