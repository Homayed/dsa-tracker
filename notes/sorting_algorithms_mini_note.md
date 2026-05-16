# Sorting Algorithms Mini Note

Sorting means arranging values in order.

Example:
[3, 1, 2] becomes [1, 2, 3]

Sorting is important because sorted data makes searching easier, especially binary search.

## Selection Sort

Selection sort repeatedly finds the smallest value and places it at the front.

Example:
[3, 1, 2]

Find smallest: 1
Move it to the front:
[1, 3, 2]

Then sort the rest:
[1, 2, 3]

Time Complexity: O(n²)
Space Complexity: O(1)

Main idea:
Select the smallest remaining value each time.

## Merge Sort

Merge sort uses divide and conquer.

It splits the list into smaller halves until each part has one item.

Then it merges the sorted parts back together.

Example:
[4, 2, 1, 3]

Split:
[4, 2] and [1, 3]

Split again:
[4], [2], [1], [3]

Merge sorted:
[2, 4] and [1, 3]

Merge again:
[1, 2, 3, 4]

Time Complexity: O(n log n)
Space Complexity: O(n)

Main idea:
Split first, then merge sorted parts.

## Quick Sort

Quick sort chooses a pivot value.

Values smaller than the pivot go to one side.

Values greater than the pivot go to the other side.

Then the same idea is applied again to each side.

Average Time Complexity: O(n log n)
Worst Time Complexity: O(n²)
Space Complexity: depends on implementation

Main idea:
Choose a pivot and partition the array around it.

