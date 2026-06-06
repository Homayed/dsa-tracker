# Merge Sorted Array Review

Pattern:
Two pointers / Array merging / In-place update

Main idea:
We are given two sorted arrays.
nums1 has extra space at the end.
We need to merge nums2 into nums1 in sorted order.

Important:
nums1 has length m + n.
Only the first m values in nums1 are real.
nums2 has n values.

Example:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Review Again:
Merge Sorted Array

Reason:
The three-pointer approach is new/confusing.

Focus:
p1 = last real value in nums1
p2 = last value in nums2
p  = last position in nums1

Key idea:
Compare from the back and place the bigger value at nums1[p].

Real nums1 part:
[1,2,3]

Final result:
[1,2,2,3,5,6]

Simple approach:
Take nums1[:m], combine with nums2, sort, then assign back to nums1[:].

Better approach:
Use three pointers from the end.

Time Complexity:
O(m+n) for the three-pointer approach

Space Complexity:
O(1)

Mistake to remember:
nums1[:m] means only the real values of nums1.
nums1[:] = ... modifies the original nums1 in-place.

Review Again:
Merge Sorted Array

Reason:
The three-pointer approach is new/confusing.

Focus:
p1 = last real value in nums1
p2 = last value in nums2
p  = last position in nums1

Key idea:
Compare from the back and place the bigger value at nums1[p].