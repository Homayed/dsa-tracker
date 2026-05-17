Introduction: Insertion Sort

Today I reviewed the Introduction: Insertion Sort section from CU Boulder Module 1. This section connects with CLRS Chapter 2, especially the insertion sort explanation and pseudocode.

What is Insertion Sort?

Insertion sort is a simple sorting algorithm that builds a sorted portion of the array from left to right.

The main idea is:

Take the current element.
Compare it with the sorted part on the left.
Shift bigger elements to the right.
Insert the current element into the correct position.

It works like sorting cards in your hand. You keep the left side sorted and insert each new card into the correct position.

Sorted Portion Idea

In insertion sort, the left side of the array is treated as already sorted.

Example:

[5, 2, 4, 6, 1, 3]

At the beginning:

[5] is the sorted portion.

Then insertion sort takes 2 and inserts it into the correct place:

[2, 5]

Then it takes 4 and inserts it between 2 and 5:

[2, 4, 5]

This continues until the whole array becomes sorted.

CLRS Pseudocode Idea

CLRS uses this idea:

INSERTION-SORT(A)

for j = 2 to A.length
    key = A[j]
    i = j - 1

    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1

    A[i + 1] = key

CLRS uses 1-based indexing, while Python uses 0-based indexing.

So in Python:

CLRS A[1] = Python arr[0]
CLRS A[2] = Python arr[1]
Key Variable

The key is the current value that needs to be inserted into the correct position.

Example:

[5, 2, 4, 6, 1, 3]

When the current value is 2:

key = 2

Then insertion sort compares key with the sorted left side.

Shifting Bigger Values

This part is very important:

A[i + 1] = A[i]

This means:

Move the bigger value one step to the right.

Example:

[5, 2, 4, 6, 1, 3]

If key = 2, then 5 > 2.

So 5 shifts right:

[5, 5, 4, 6, 1, 3]

The value 2 is not lost because it is stored in key.

Then key is placed into the correct position:

[2, 5, 4, 6, 1, 3]
Python Code I Practiced

I coded insertion sort in:

practice/insertion_sort.py

The main idea in my code was:

arr[i + 1] = arr[i]

This shifts the bigger value to the right.

Then:

arr[i + 1] = key

This inserts the key into the correct position.

Important Lesson from the Quiz

I completed the insertion sort quiz and got 100%.

The main thing I understood:

The number of swaps/shifts depends on how many previous elements are greater than the key.

If the current element is already greater than the last value in the sorted portion, then no shift is needed.

If there are bigger values before it, those bigger values must shift right.

Example from Quiz Thinking

For an almost sorted array:

[1, 2, 7, 4, 5, 6, 3, 8, 9]

The sorted portion grows step by step.

When inserting 7 into:

[1, 2]

no shift is needed because:

2 < 7

When inserting 4, 5, and 6, each one only needs to move past 7.

When inserting 3, it needs to move past all bigger values before it:

7, 6, 5, 4

So the number of shifts equals the number of previous elements greater than the key.

Time Complexity

Insertion sort has different running times depending on the input.

Best Case

If the array is already sorted:

[1, 2, 3, 4, 5]

Then insertion sort does very little shifting.

Best case: O(n)
Worst Case

If the array is reverse sorted:

[5, 4, 3, 2, 1]

Then every new element must move all the way to the front.

Worst case: O(n²)
Average Case

For a random unsorted array:

Average case: O(n²)
Space Complexity

Insertion sort sorts the array in-place.

It only uses a few extra variables:

key
i
j

So:

Space complexity: O(1)
Main Takeaways
Insertion sort builds a sorted left side.
The current value is stored as key.
Bigger values shift right.
The key is inserted into the correct position.
The number of shifts depends on how many previous values are greater than the key.
Insertion sort is good for small or nearly sorted arrays.
Best case is O(n).
Worst case is O(n²).
Space complexity is O(1).
My Understanding

Today I understood insertion sort more clearly through CLRS and the CU Boulder module. I now understand why arr[i + 1] = arr[i] shifts a bigger value to the right, and why arr[i + 1] = key places the current value into the correct position.

I also understood that insertion sort is efficient when the array is already sorted or almost sorted, but slow when the array is reverse sorted.