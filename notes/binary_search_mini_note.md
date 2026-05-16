# Binary Search Mini Note

Binary search works on sorted arrays.

Instead of checking every number one by one, it checks the middle.

If the target is bigger than the middle value, search the right half.

If the target is smaller than the middle value, search the left half.

This is why binary search is O(log n), because the search area gets cut in half each time.

Variables:
left = start index
right = end index
mid = middle index

Formula:
mid = (left + right) // 2