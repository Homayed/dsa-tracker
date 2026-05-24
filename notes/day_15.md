# Day 15 — Container With Most Water, Module 2 Review Plan, and MLH Preparation

## Date
24 May 2026

## Main Focus

Today was focused on continuing the roadmap after completing the Day 22-level tasks.

Previously, I completed:

- 3Sum
- CU Boulder Algorithms Module 2
- Module 2 assignments
- Day 14 note
- Module 2 notes

Today I moved forward into the next roadmap task:

- Container With Most Water
- Two Pointers pattern
- Module 2 assignment review planning
- Heap basics review
- MLH Fellowship preparation discussion
- Global / multinational remote work direction

---

# 1. Roadmap Status

## Completed Before Today
Completed Today
Container With Most Water ✅
Added / ready to add to DSA tracker ✅
Module 2 heap review plan prepared ✅
MLH preparation direction clarified ✅
Current Position

I am ahead of the original roadmap in DSA / LeetCode.

I have already completed some problems that were planned later, including:

Valid Parentheses
Min Stack
Evaluate Reverse Polish Notation
3Sum
Container With Most Water

Now I need to keep balancing:

CU Boulder coursework
LeetCode / DSA
DSA Tracker project
MLH / global remote career preparation
2. Problem Completed Today — Container With Most Water
Problem

Given a list of heights, find two lines that can hold the most water.

The area is calculated as:

Area = width × height

Where:

width = right - left
height = min(height[left], height[right])
Topic

Two Pointers

Pattern

Left pointer + right pointer / move the smaller height

Main Idea

Start with two pointers:

left = 0
right = len(height) - 1

The widest container starts from both ends.

At each step:

width = right - left
current_height = min(height[left], height[right])
area = width * current_height

Then update the maximum area.

The pointer movement rule is:

Move the pointer with the smaller height.

Reason:

The water level is limited by the shorter line.

If the left side is shorter, move left.

If the right side is shorter, move right.

Final Code
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maximum_n = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            if area > maximum_n:
                maximum_n = area

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return maximum_n
Complexity
Time Complexity: O(n)
Space Complexity: O(1)

Reason:

Only one pass is needed because either left or right moves every loop.

No extra data structure is used.

What I Learned
Area depends on both width and height.
The shorter height limits the water.
Moving the taller side does not help if the shorter side is still limiting.
Two pointers work because the array is scanned from both ends.

Main memory line:

Area = (right - left) * min(height[left], height[right])
Move the smaller height pointer.
3. DSA Tracker Entry

Add this to the tracker:

Problem: Container With Most Water
Difficulty: Medium
Topic: Two Pointers
Pattern: Left pointer + right pointer / move smaller height
Time Complexity: O(n)
Space Complexity: O(1)
Note file: notes/day_15.md
Status: Completed
4. Heap Review — Python heapq

Today I also reviewed how to convert an array / list into a heap in Python.

Min Heap

Python has a built-in heap module:

import heapq

To convert a list into a min heap:

arr = [5, 3, 8, 1, 2]
heapq.heapify(arr)

After heapify:

arr[0]

is the smallest element.

Important:

A heap is not fully sorted.
It only follows the heap property.

For Python heapq:

Smallest element is at index 0.

This is different from my CU Boulder assignment heap, where:

self.H = [None]

means the real heap starts from index 1.

Max Heap in Python

Python heapq is a min heap by default.

To simulate a max heap:

max_heap = [-x for x in arr]
heapq.heapify(max_heap)
largest = -heapq.heappop(max_heap)

Memory:

Python heapq = min heap
Use negative values to simulate max heap
5. Module 2 Assignment Review Plan

I completed Module 2 and all assignments, but I need to revise the code properly.

The correct review order is:

1. MinHeap
2. MaxHeap
3. TopKHeap
4. MedianMaintainingHeap

Do not start from MedianMaintainingHeap first because it is the hardest.

MinHeap Review Target

Understand:

parent <= child
smallest value stays at root
insert uses bubble_up
delete_min uses bubble_down

Important index rules:

parent = index // 2
left_child = 2 * index
right_child = 2 * index + 1
MaxHeap Review Target

Understand:

parent >= child
largest value stays at root
insert uses bubble_up
delete_max uses bubble_down

Difference from MinHeap:

MinHeap swaps with smaller child.
MaxHeap swaps with bigger child.
TopKHeap Review Target

Understand:

A = smallest k elements, sorted
H = remaining larger elements, stored in MinHeap

Important rule:

Every element in A <= every element in H

Insertion logic:

If A has fewer than k items:
    insert into A

If A is full and new element is smaller than A[-1]:
    new element enters A
    old largest from A moves to H

Otherwise:
    new element goes to H
MedianMaintainingHeap Review Target

Understand:

hmax = lower half
hmin = upper half

Rules:

hmax.max_element() <= hmin.min_element()
hmin can have same size as hmax or one extra

Median logic:

If same size:
    median = average of hmax.max and hmin.min

If hmin has one extra:
    median = hmin.min
6. MLH Fellowship Preparation Discussion

Today I also clarified my MLH and global career direction.

Goal

I do not want ordinary Bangladeshi local jobs unless they are multinational or globally relevant.

My target is:

Global remote experience
Multinational companies
Open-source fellowships
Remote internships
Remote Python / backend roles
MLH Fellowship
GSoC
LFX Mentorship
MLH Direction

The best MLH direction for me is:

MLH Fellowship — Software Engineering / Open Source Track

Not Production Engineering / SRE yet, because that needs more Linux, networking, backend services, deployment, and infrastructure.

Main MLH Project

My main MLH project should be:

DSA Tracker CLI

Because it already shows:

Python
JSON
CLI app structure
add / view / search / delete
stats feature
GitHub commits
real personal use-case
roadmap discipline

But before MLH, I need to polish it.

DSA Tracker Improvements Needed
1. Improve README
2. Add screenshots or terminal examples
3. Add topic filter
4. Add topic count
5. Add pattern count
6. Add review-needed status
7. Add clear installation / run instructions
8. Clean GitHub profile
Future Strong MLH Project

Later, I should build:

DSA Tracker API with FastAPI

This means converting the tracker from a CLI app into a backend API.

Example routes:

GET /problems
POST /problems
GET /problems/topic/{topic}
GET /stats
DELETE /problems/{id}

This will show:

Python backend
FastAPI
JSON / API design
HTTP basics
real project structure
README documentation

This will make the MLH application stronger.

7. Career Direction

My goal is:

CU Boulder MS-CS
+ LeetCode / DSA
+ DSA Tracker
+ GitHub projects
+ MLH / open-source fellowship
+ global remote sector work
+ FAANG / multinational preparation

I should avoid:

ordinary local jobs
random non-tech jobs
low-value microtasks
roles requiring US-only work authorization
roles requiring 3+ years experience

I should target:

MLH Fellowship
GSoC
LFX Mentorship
Outreachy if eligible
Global remote QA / testing
Remote Python internships
Remote backend internships
Remote software support roles
Multinational internships
8. Current Readiness Reflection

Current rough readiness:

Global remote QA / testing: improving
MLH readiness: early but realistic
Python automation: improving
Backend internship: not ready yet
FAANG: long-term target

Main weakness:

Need stronger GitHub proof
Need project polish
Need CV
Need FastAPI / backend basics later
Need more explanation practice
9. What I Need To Do Next
Immediate Next Steps
1. Add Container With Most Water to DSA tracker
2. Save day_15.md
3. Push to GitHub
4. Revise Module 2 heaps on Day 24
5. Start improving DSA Tracker README soon
Next Roadmap Task
Day 24:
Module 2 revision / course notes review

Main revision topics:

Hash tables
Chaining
MinHeap
MaxHeap
TopKHeap
MedianMaintainingHeap
10. Final Reflection

Today was a strong continuation day.

I completed Container With Most Water, which strengthens the Two Pointers pattern after 3Sum.

I also clarified how Module 2 should be reviewed and how MLH Fellowship preparation fits into my long-term goal.

The main lesson today:

Solving problems is not enough.
I need to turn my work into visible proof through GitHub, README files, projects, and clear explanations.

Current progress:

3Sum ✅
Container With Most Water ✅
CU Boulder Module 2 ✅
Module 2 assignments ✅
DSA Tracker growing ✅
MLH direction clarified ✅

Tomorrow’s focus:

Module 2 revision
Heap dry runs
DSA Tracker cleanup if time
```text
Day 22 LeetCode task: 3Sum ✅
Day 22 CU Boulder task: Module 2 ✅
Module 2 assignments ✅
3Sum added to DSA tracker ✅