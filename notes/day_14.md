# Day 14 — Roadmap Catch-Up, 3Sum, Stack Review, Heap Review, and CU Boulder Module 2

## Date
23 May 2026

## Main Focus

Today was a big roadmap progress day.

I reviewed several DSA problems, completed 3Sum, continued CU Boulder Algorithms for Searching, Sorting, and Indexing, and finished Module 2 with assignments.

This day connects directly to the roadmap’s Day 22 target:

- Continue Algorithms Module 2
- Solve LeetCode 3Sum
- Write the link between course concept and LeetCode

I am ahead of the original roadmap in DSA/LeetCode, but now I am aligning the CU Boulder course side properly.

---

# 1. Problems Reviewed Today

## Top K Frequent Elements — Sorting Version

### Topic
Arrays & Hashing

### Pattern
Hash Map + Sorting

### Main Idea
Count the frequency of each number using a dictionary, then sort the keys based on frequency.

### Key Code Idea

```python
sorted_keys = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)
return sorted_keys[:k]

What I Reviewed
dic[num] = 1
dic[num] += 1
dic.keys()
key=lambda x: dic[x]
reverse=True
returning top k elements
Complexity
Time: O(n + m log m)
Space: O(m)
Valid Parentheses
Topic

Stack

Pattern

Stack + Matching Pairs

Main Idea

Opening brackets go into the stack. Closing brackets must match the most recent opening bracket.

Key Rules
Opening bracket -> push
Closing bracket -> check stack[-1]
Wrong match -> return False
Correct match -> pop
End -> stack must be empty
Key Dictionary
dic = {
    ")": "(",
    "}": "{",
    "]": "["
}
What I Reviewed
Why else means current bracket is a closing bracket
Why if not lst is needed
Why lst[-1] != dic[bracket] means mismatch
Why we only return True at the end
Complexity
Time: O(n)
Space: O(n)
Longest Consecutive Sequence
Topic

Arrays & Hashing

Pattern

Hash Set

Main Idea

Use a set to check whether numbers exist quickly.

Only start counting when the number is the beginning of a sequence.

Key Line
if num - 1 not in current_nums:

This means the current number has no previous number, so it is the start of a sequence.

Key Loop
while current_num + 1 in current_nums:

This means keep counting while the next number exists.

Final Reviewed Code
class Solution(object):
    def longestConsecutive(self, nums):
        longest = 0 
        current_nums = set(nums)

        for num in current_nums:
            if num - 1 not in current_nums:
                current_num = num
                count = 1

                while current_num + 1 in current_nums:
                    current_num += 1
                    count += 1

                if count > longest:
                    longest = count

        return longest
Complexity
Time: O(n)
Space: O(n)
Min Stack
Topic

Stack

Pattern

Stack Design / Two Stacks

Main Idea

Use two stacks:

lst -> stores real values
min_lst -> stores current minimum at each step
Final Reviewed Code
class MinStack(object):

    def __init__(self):
        self.lst = []
        self.min_lst = []

    def push(self, val):
        self.lst.append(val)

        if not self.min_lst:
            self.min_lst.append(val)
        else:
            current_min = min(val, self.min_lst[-1])
            self.min_lst.append(current_min)

    def pop(self):
        self.lst.pop()
        self.min_lst.pop()

    def top(self):
        return self.lst[-1]

    def getMin(self):
        return self.min_lst[-1]
What I Reviewed
self.lst
self.min_lst
why getMin() should not loop
why pop() removes from both stacks
why min_lst[-1] gives O(1) minimum
Complexity
push: O(1)
pop: O(1)
top: O(1)
getMin: O(1)
Space: O(n)
Top K Frequent Elements — Heap Version
Topic

Arrays & Hashing / Heap

Pattern

Hash Map + Min Heap

Main Idea

Count frequencies, then keep a min heap of size k.

If heap size becomes greater than k, pop the smallest frequency.

Key Code Idea
heapq.heappush(heap, (freq, num))

if len(heap) > k:
    heapq.heappop(heap)
What I Reviewed
Python heap is a min heap
push (freq, num)
heap keeps only top k frequent numbers
remember to return result
Complexity
Time: O(n + m log k)
Space: O(m)
Top K Frequent Elements — Bucket Sort Version
Topic

Arrays & Hashing

Pattern

Hash Map + Bucket Sort

Main Idea

Use frequency as the bucket index.

bucket[frequency] = list of numbers with that frequency
Key Line
bucket[freq].append(num)

This means put the number into the bucket that represents its frequency.

Reviewed Code
class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

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
What I Reviewed
dictionary stores number -> frequency
bucket stores frequency index -> numbers
scan from highest frequency to lowest
stop when result length equals k
Complexity
Time: O(n)
Space: O(n)
Evaluate Reverse Polish Notation
Topic

Stack

Pattern

Stack / Expression Evaluation

Main Idea

Numbers go into the stack. Operators pop the last two numbers, calculate, and push the result back.

Key Rule
right = stack.pop()
left = stack.pop()

Then calculate:

left operator right

This matters for subtraction and division.

Final Code
class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for c in tokens:
            if c not in ["+", "-", "*", "/"]:
                stack.append(int(c))

            else:
                right = stack.pop()
                left = stack.pop()

                if c == '+':
                    result = left + right
                elif c == '-':
                    result = left - right
                elif c == '*':
                    result = left * right
                elif c == '/':
                    result = int(float(left) / right)

                stack.append(result)

        return stack[-1]
Complexity
Time: O(n)
Space: O(n)
2. New Problem Completed Today — 3Sum
Problem

Given an integer array, return all unique triplets that sum to zero.

Example:

nums = [-1, 0, 1, 2, -1, -4]

Answer:

[[-1, -1, 2], [-1, 0, 1]]
Topic

Two Pointers

Pattern

Sort + Fixed Pointer + Left/Right Pointers

Main Idea

First sort the array.

Then fix one number and use two pointers to find the other two numbers.

fixed = first number
left = second number
right = third number

If total is too small, move left right.

If total is too big, move right left.

Final Code
class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        result = []

        for fixed in range(len(nums)):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue

            left = fixed + 1
            right = len(nums) - 1

            while left < right:
                total = nums[fixed] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[fixed], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result
Key Pointer Movement
total == 0 -> save triplet, move both
total < 0  -> move left right
total > 0  -> move right left
Complexity
Time: O(n²)
Space: O(1), excluding output
What I Learned

3Sum is not solved by checking random combinations.

The sorted array allows the two pointers to move intelligently.