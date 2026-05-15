# Day 6 Progress

Today I solved **Move Zeroes** and learned more about **in-place array modification**.

In this problem, I first understood that all non-zero numbers should stay in the same order, while all zeroes should be moved to the end of the list. The important part was that LeetCode does not want a returned list. It wants the original `nums` list to be modified directly.

At first, I separated the numbers into two lists: one list for non-zero values and another list for zeroes. Then I combined them into a new list. This helped me understand the logic clearly: keep the useful numbers first, then place the zeroes at the end.

The main thing I learned was the meaning of:

```python
nums[:] = reformed_list
```

I understood that `nums[:]` means the whole original list. So when I write `nums[:] = reformed_list`, I am replacing the contents of the original `nums` list instead of creating a new local list. This is important because LeetCode checks whether the original input list was changed.

Main lessons:

* Move Zeroes requires modifying the list in-place.
* Returning a new list is not enough for this problem.
* Non-zero values should keep their original order.
* Zeroes should be moved to the end.
* `nums[:]` means the whole original list.
* `nums[:] = reformed_list` replaces the original list contents.
* `nums = reformed_list` only changes the local variable, not the original list LeetCode checks.
* Some array problems are about modifying the input directly.

Pattern learned:
In-place array modification

Project improvement:
Added **Move Zeroes** to the DSA Tracker.

Big-O understanding:

* Looping through `nums` takes `O(n)` time.
* Creating `non_zero`, `zero`, and `reformed_list` uses extra space.
* Time complexity: `O(n)`
* Space complexity: `O(n)` for my current version.

Reflection:
Today I understood that some LeetCode problems do not care about what I return. Instead, they check if I changed the original input list. This helped me understand the difference between creating a new list and modifying an existing list in-place. I also became more comfortable with Python slicing, especially the meaning of `nums[:]`.
