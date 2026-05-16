# Day 7 Progress

Today I solved **Merge Sorted Array** and learned more about **array slicing** and **in-place list modification**.

In this problem, I first understood that `nums1` already has extra zeroes at the end, but those zeroes are not real values. They are only empty spaces for merging `nums2` into `nums1`. The value `m` tells me how many real numbers are inside `nums1`, and `n` tells me how many real numbers are inside `nums2`.

The important part I learned was this:

```python
nums1[:m]
```

This means take only the first `m` real values from `nums1`.

For example:

```python
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
```

Then:

```python
nums1[:m]
```

gives:

```python
[1, 2, 3]
```

So the extra zeroes are ignored.

Then I merged the real part of `nums1` with `nums2`:

```python
nums1[:m] + nums2
```

After that, I sorted the merged list and used:

```python
nums1[:] = sorted(nums1[:m] + nums2)
```

I understood that `nums1[:]` means the whole original list. So assigning to `nums1[:]` modifies the original `nums1` list in-place, which is what LeetCode requires.

Main lessons:

* In this problem, the zeroes at the end of `nums1` are placeholders.
* `m` tells how many real values are in `nums1`.
* `nums1[:m]` keeps only the real values from `nums1`.
* `nums1[:]` means the whole original list.
* `nums1[:] = ...` modifies the original list in-place.
* Returning a new list is not enough because LeetCode checks the original `nums1`.
* Sorting after merging is a simple valid approach.
* Slicing helps control which part of a list I want to use.

Pattern learned:
Array slicing + in-place update

Project improvement:
Added **Merge Sorted Array** to the DSA Tracker.

Big-O understanding:

* `nums1[:m] + nums2` creates a merged list of size `m + n`.
* Sorting the merged list takes `O((m+n) log(m+n))` time.
* Space complexity is `O(m+n)` because a new merged list is created before copying it back into `nums1`.

Reflection:
Today I understood the difference between the real values in an array and placeholder values. I also became more comfortable with Python slicing. The biggest lesson was that `nums1[:m]` is used to select only the meaningful part of the list, while `nums1[:] = ...` is used to update the original list itself. This helped me understand in-place modification more clearly.

code:

nums1[:] = sorted(nums1[:m] + nums2)

Pattern: Array slicing + in-place update
Data structure: List
Time Complexity: O((m+n) log(m+n))
Space Complexity: O(m+n)
Main idea: Use nums1[:m] to keep only the real values from nums1, merge them with nums2, sort the result, then use nums1[:] to update the original nums1 list in-place.

