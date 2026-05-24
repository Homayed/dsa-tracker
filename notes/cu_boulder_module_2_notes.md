CU Boulder Module 2 Completed
Course

Algorithms for Searching, Sorting, and Indexing

Module

Module 2

Status

Completed Module 2 and all assignments.

Main Areas Covered
Hashtable / hash table ideas
Hash function
Chaining
Insertion cost
MinHeap
MaxHeap
TopKHeap
MedianMaintainingHeap
Heap balancing
Using heaps for efficient operations
4. Hashtable Question Reviewed
Concept

A hash table stores key-value pairs.

Example:

Apples -> 51

Apples is the key.
51 is the value.

Collision Handling

If multiple keys go to the same slot, they are stored in a chained list.

Insert Cost

To insert a new item:

1. Run HASH
2. Check every existing item in that slot's chain
3. Write the new item at the end

Formula:

Total cost = 1 for HASH + number of items in that slot + 1 for writing
5. Heap Assignments / Code Completed
MinHeap

I completed:

insert
delete_min
Main Idea
insert:
append at end, then bubble up

delete_min:
remove root, move last item to root, bubble down
MaxHeap

I completed:

bubble_up
bubble_down
insert
delete_max
Main Idea

MaxHeap is the opposite of MinHeap.

MaxHeap rule:
parent >= child

The maximum element is always at:

self.H[1]
TopKHeap

I worked on a structure that keeps:

A = smallest k elements, sorted
H = remaining larger elements, stored in min heap
Main Idea

When inserting:

If A has fewer than k items -> insert into A
If A is full and new item is smaller than A's largest -> replace A's largest and move old largest to heap
Otherwise -> insert into heap

When deleting from top k:

Remove from A
Move smallest element from heap into A
Keep A sorted
MedianMaintainingHeap

I worked on:

get_median
balance_heap_sizes
insert
delete_median
Main Idea

Use two heaps:

hmax = lower half of numbers
hmin = upper half of numbers

Rules:

hmax.max_element() <= hmin.min_element()
hmin can have the same size as hmax or one extra

Median:

If same size:
average of hmax.max and hmin.min

If hmin has one extra:
hmin.min
6. Roadmap Status
Completed / Ahead
Top K Frequent Elements
Longest Consecutive Sequence
Two Sum II
Valid Parentheses
Min Stack
Evaluate Reverse Polish Notation
3Sum
CU Boulder Module 2
Module 2 assignments
Tracker updates
GitHub pushes
Current Position

I am ahead of the original LeetCode/DSA roadmap.

The Day 22 coding task was 3Sum, and I completed it.

The Day 22 CU Boulder task was Module 2, and I completed Module 2 with assignments.

7. Weak Areas To Review
3Sum duplicate skipping
Heap balancing
MedianMaintainingHeap
TopKHeap
Bucket sort
RPN operator order
8. Tomorrow’s Next Step

Next roadmap task:

Day 23 — Container With Most Water

Topic:

Two Pointers

Pattern:

Left pointer + right pointer
Move the pointer with the smaller height

Before starting, I should briefly review:

3Sum
Module 2 heap notes
MedianMaintainingHeap
Final Reflection

Today was a strong day.

I completed 3Sum and finished CU Boulder Module 2 with assignments.

I also reviewed multiple important DSA patterns:

Hash Map
Hash Set
Stack
Heap
Two Pointers
Bucket Sort

This is strong evidence that I am ahead of the original roadmap in DSA, while now also keeping the CU Boulder course side aligned.


Paste this in `cu_boulder/algorithms_searching_sorting_indexing/module_2_notes.md`:

```markdown
# Module 2 Notes — Algorithms for Searching, Sorting, and Indexing

## Course
Algorithms for Searching, Sorting, and Indexing

## Module
Module 2

## Status
Completed Module 2 and all assignments.

---

# 1. Main Topics

Module 2 focused heavily on data structures that support efficient searching, indexing, priority access, and median/top-k maintenance.

Main topics covered:

```text
Hash tables
Hash functions
Chaining
Insertion cost
MinHeap
MaxHeap
TopKHeap
MedianMaintainingHeap
Heap balancing
2. Hash Tables
What is a Hash Table?

A hash table stores key-value pairs.

Example:

Apples -> 51

Here:

Key = Apples
Value = 51

A hash function decides which slot the key should go into.

Hash Function

A hash function takes a key and returns a slot/index.

Example idea:

HASH(key) -> slot number

In the produce example, the hash function used the ASCII value of the first letter modulo 5.

Example:

Apples -> A -> ASCII 65
65 mod 5 = 0

So Apples goes to Slot 0.

Collision

A collision happens when two or more keys go to the same slot.

Example:

Apples
Plums
Avocados

All may share the same slot.

Chaining

Chaining means storing multiple entries in a list at the same slot.

Example:

Slot 0:
Apples -> Plums -> Avocados
Insertion Cost

To insert a new key-value pair:

1. Run HASH
2. Go to the correct slot
3. Check every existing item in that slot
4. Insert the new item at the end

If HASH costs 1, each check costs 1, and writing costs 1:

Total cost = 1 + number of items in chain + 1

So:

Total cost = number of items in chain + 2
3. MinHeap
Main Rule

In a MinHeap:

Parent <= child

The smallest element is always at the root.

Because this heap implementation uses:

self.H = [None]

the real heap starts from index 1.

So the minimum element is:

self.H[1]
Bubble Up

Used after insertion.

If the child is smaller than the parent, swap upward.

Insert at end
Compare with parent
Swap if needed
Repeat
Bubble Down

Used after deleting the minimum.

Move last element to root
Compare with children
Swap with smaller child
Repeat
MinHeap Insert
def insert(self, elt):
    self.H.append(elt)
    self.bubble_up(self.size())
MinHeap Delete Min
def delete_min(self):
    assert self.size() > 0

    min_elt = self.H[1]

    if self.size() == 1:
        self.H.pop()
        return min_elt

    self.H[1] = self.H.pop()
    self.bubble_down(1)

    return min_elt
4. MaxHeap
Main Rule

In a MaxHeap:

Parent >= child

The largest element is always at the root.

self.H[1]
Difference From MinHeap

MinHeap keeps the smallest at the root.

MaxHeap keeps the largest at the root.

MaxHeap Insert
Append at end
Bubble up if child is bigger than parent
MaxHeap Delete Max
Save root
Move last element to root
Bubble down
Return saved root
5. TopKHeap
Main Idea

TopKHeap keeps the smallest k elements separately.

A = smallest k elements, sorted
H = remaining larger elements, stored in MinHeap
Invariant
A is sorted
H is a min heap
Every element in A <= every element in H
Insert Logic

If total size is less than k:

insert into A
keep A sorted

If A already has k elements:

If new element < largest element in A:
    replace largest in A
    move old largest to H
Else:
    insert new element into H
Delete From Top K

To delete the j-th element from A:

Remove A[j]
Take min from H
Insert it back into A
Keep A sorted
6. MedianMaintainingHeap
Main Idea

Use two heaps to maintain the median efficiently.

hmax = lower half
hmin = upper half
Invariants
hmax.max_element() <= hmin.min_element()
hmin size == hmax size
OR
hmin size == hmax size + 1

This means hmin can have one extra element.

Median Logic

If both heaps have the same size:

median = average of hmax.max_element() and hmin.min_element()

If hmin has one extra:

median = hmin.min_element()
Balance Heap Sizes

If hmax becomes larger:

move hmax.delete_max() into hmin

If hmin becomes too large:

move hmin.delete_min() into hmax
Insert Logic

If new element belongs to the upper half:

insert into hmin

If it belongs to the lower half:

insert into hmax

Then rebalance heap sizes.

7. Connection to LeetCode
Top K Frequent Elements

The heap idea connects directly to Top K Frequent Elements.

In LeetCode, I used:

heapq.heappush(heap, (freq, num))

The heap kept only the top k frequent elements.

3Sum

3Sum connects to sorting and search strategy.

After sorting, two pointers can move intelligently:

If total < 0, move left to get a bigger number
If total > 0, move right to get a smaller number

So sorting changes the problem from random searching into structured searching.

Longest Consecutive Sequence

Hash tables/sets connect directly to Longest Consecutive Sequence.

A set allows fast existence checks:

num in num_set

This helps check:

num - 1 not in num_set
current_num + 1 in num_set
8. What I Understood
Hash tables are useful for fast lookup.
Chaining handles collisions.
Heap root gives quick access to min or max.
MinHeap keeps smallest at root.
MaxHeap keeps largest at root.
Two heaps can maintain median efficiently.
TopKHeap separates top k elements from the rest.
9. What Was Difficult
TopKHeap logic
MedianMaintainingHeap balancing
Understanding which heap stores lower half and upper half
Remembering when to bubble up vs bubble down
Understanding deletion and replacement logic
10. Key Memory Lines
Hash table = key-value storage with fast lookup
Collision = multiple keys in same slot
Chaining = list inside a slot
MinHeap = parent <= child
MaxHeap = parent >= child
hmax = lower half
hmin = upper half
Median = middle value using heap roots