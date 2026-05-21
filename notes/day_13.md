# Day 13 — Longest Consecutive Sequence, Min Stack, and Online Tech Work Setup

## Today's Focus

Today and yesterday were focused on cleaning up my DSA roadmap, solving important interview problems, and starting my fully online tech-work setup.

Main topics covered:

- Longest Consecutive Sequence
- Hash Set vs Hash Map
- Min Stack
- Stack design using two stacks
- uTest setup
- Fully online tech-work direction
- CU Boulder payment/admission questions

---

# 1. Longest Consecutive Sequence

## Problem

Given an unsorted array of integers, return the length of the longest consecutive sequence.

Example:

```python
nums = [100, 4, 200, 1, 3, 2]
```

The longest consecutive sequence is:

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

## First Mistake

At first, I tried to solve it using a dictionary and counting logic.

I was thinking about frequency, but this problem is not about frequency.

For this problem, I do not need to know how many times a number appears.

I only need to know:

```text
Does this number exist?
Does the next number exist?
Does the previous number exist?
```

So the correct structure is a set, not a frequency dictionary.

---

## Hash Set vs Hash Map

## Hash Map

In Python, a hash map is a dictionary.

Example:

```python
dic = {
    1: 3,
    2: 2,
    3: 1
}
```

This stores:

```text
key -> value
```

So a hash map is useful when I need to store information about something.

Example:

```text
1 appears 3 times
2 appears 2 times
3 appears 1 time
```

Used in problems like:

```text
Top K Frequent Elements
Two Sum
Group Anagrams
Contains Duplicate II
```

---

## Hash Set

In Python, a hash set is a set.

Example:

```python
num_set = {1, 2, 3, 4}
```

A set only stores values.

It is useful when I only need to check whether something exists.

Example:

```python
2 in num_set
```

returns:

```python
True
```

Used in problems like:

```text
Contains Duplicate
Longest Consecutive Sequence
Intersection problems
```

---

## Main Idea

Use a set for fast lookup.

```python
num_set = set(nums)
```

The most important line is:

```python
if num - 1 not in num_set:
```

This means:

```text
Only start counting if the current number is the beginning of a sequence.
```

Example:

```text
1 -> 0 not in set, so start counting
2 -> 1 is in set, so do not start
3 -> 2 is in set, so do not start
4 -> 3 is in set, so do not start
```

So for the sequence:

```text
1, 2, 3, 4
```

I only start from `1`.

---

## Final Code

```python
class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_count = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_count += 1

                if current_count > longest:
                    longest = current_count

        return longest
```

---

## Complexity

```text
Time Complexity: O(n)
Space Complexity: O(n)
```

Reason:

```text
The set stores all numbers.
Each number is checked efficiently.
We only start counting from the beginning of each sequence.
```

---

## What I Learned

```text
Hash Set is used when I only care about existence.
Hash Map is used when I need key-value information.
Longest Consecutive Sequence is not a frequency problem.
The key is finding the start of the sequence.
```

---

# 2. Min Stack

## Problem

Design a stack that supports:

```python
push(val)
pop()
top()
getMin()
```

The special requirement is:

```text
getMin() must return the minimum value in O(1).
```

---

## Topic

Stack

## Pattern

Stack Design / Two Stacks

---

## First Mistake

At first, I tried to create the object inside the class and used variables like:

```python
obj
lst
val
```

But in class-based problems, LeetCode creates the object automatically.

Inside the class, I need to use:

```python
self
```

Example:

```python
self.stack = []
```

This means the stack belongs to the current object.

---

## Main Idea

Use two stacks:

```text
stack     -> stores all values
min_stack -> stores the minimum value at each step
```

The reason for `min_stack` is that `getMin()` must be O(1).

If I loop through the whole stack every time, `getMin()` becomes O(n), which is not accepted.

---

## Example

```python
push(5)
```

```text
stack     = [5]
min_stack = [5]
```

```python
push(3)
```

```text
stack     = [5, 3]
min_stack = [5, 3]
```

```python
push(7)
```

Current minimum is still `3`.

```text
stack     = [5, 3, 7]
min_stack = [5, 3, 3]
```

So:

```python
getMin()
```

returns:

```python
self.min_stack[-1]
```

which is:

```text
3
```

---

## Final Code

```python
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

---

## Complexity

```text
push: O(1)
pop: O(1)
top: O(1)
getMin: O(1)

Space Complexity: O(n)
```

---

## What I Learned

```text
self.stack stores the real values.
self.min_stack stores the minimum value at every step.
Every push should update both stacks.
Every pop should remove from both stacks.
getMin() should not loop through the stack.
```

---

# 3. Online Tech Work Setup

## Goal

I want to earn in my sector, not just earn random money.

My goal is:

```text
Fully online tech-related work
```

Not local work, not physical work.

---

## Best First Online Tech Direction

The best first path is:

```text
Manual QA testing
```

Because it is tech-related and beginner-friendly.

It can help me learn:

```text
bug reporting
test cases
software behaviour
technical communication
attention to detail
```

Later, this can grow into:

```text
QA Automation
Python testing
pytest
Selenium
Playwright
API testing
```

---

## uTest Setup

I created my uTest account and started looking at the Academy/courses.

Best starting order:

```text
1. uTest Academy
2. Bug Reporting
3. Test Cases
4. Practice Test Cycle
```

I should avoid advanced topics for now, such as:

```text
API Testing
Automation
Security Testing
Charles Proxy
Payment Testing
```

Those can come later.

---

## uTest About Me Direction

My profile should position me as:

```text
Beginner QA Tester | Python Learner | Detail-Oriented Software Tester
```

The idea is not to pretend I am an expert.

The idea is to show that I am serious, careful, and learning software testing properly.

---

# 4. CU Boulder / Career Planning Notes

I also clarified some CU Boulder and career questions.

## CU Boulder Admission

If I complete the pathway with the required grades, admission is processed after grades post.

The key idea:

```text
Complete pathway courses
Get B or better
Declare intent
Grades post
CU processes admission
```

## Research Volunteering

I can ask professors about research volunteering later, but not too early.

Better timing:

```text
After pathway
After strong grades
After building projects
After having a clear research interest
```

I should not email vaguely.

I should email only when I can say:

```text
I am interested in your work on X.
I have built/studied Y.
I can help with Z.
```

## Fully Online Tech Work

I do not want random microtasks as the main goal.

The sector-focused order should be:

```text
1. Manual QA testing
2. QA automation later
3. Python automation projects
4. AI coding evaluation if technical
5. Junior Python/backend role later
```

---

# 5. Current Tracker / Roadmap Status

## Completed Recently

```text
Top K Frequent Elements
Valid Parentheses
Longest Consecutive Sequence
Min Stack
Tracker stats feature
Day 12 note
uTest account setup
```

## Need To Do Next

```text
Add Longest Consecutive Sequence to tracker if not already added
Write/push Longest Consecutive Sequence note
Add Min Stack to tracker
Write Min Stack note
Push latest updates to GitHub
Continue uTest Academy
```

---

# 6. Next Problem

The next problem after Min Stack should stay within the Stack roadmap.

Possible next problems:

```text
Evaluate Reverse Polish Notation
Generate Parentheses
Daily Temperatures
```

But before moving too fast, I should first:

```text
Review Min Stack
Add it to tracker
Write note
Push to GitHub
```

---

# 7. Key Lessons

## Longest Consecutive Sequence

```text
Use a set.
Only start from num - 1 not in set.
Do not think about frequency.
```

## Min Stack

```text
Use two stacks.
Main stack stores values.
Min stack stores current minimums.
getMin() should be O(1).
```

## Online Work

```text
Start with tech-related work, not random work.
uTest is a good first step.
Manual QA can lead to QA automation later.
```

---

# 8. Weak Areas To Review

```text
Hash Set problems
Dry running while loops
Stack design problems
Class-based LeetCode problems
Writing cleaner notes
Bucket Sort from Top K Frequent Elements
```

---

# 9. Weekend Review Plan

## Saturday Code Review

Review:

```text
Top K Frequent Elements
Valid Parentheses
Longest Consecutive Sequence
Min Stack
Tracker code
```

Focus on:

```text
What pattern each problem uses
Why the data structure was chosen
Time and space complexity
Code explanation out loud
```

## Sunday Module Day

Focus on:

```text
CU Boulder module work
Algorithms foundation
Recursion / sorting / binary search review
```

---

# Final Status

Today and yesterday were productive.

I completed important DSA cleanup and moved into stronger Stack and Hash Set problems.

I also started preparing for fully online tech-sector work through uTest.

Current confidence:

```text
Hash Map: better
Hash Set: improving
Stack basics: improving
Min Stack: understood
QA testing path: started
```

Next action:

```text
Add Min Stack to tracker
Write Min Stack note
Push to GitHub
Continue uTest Academy
```