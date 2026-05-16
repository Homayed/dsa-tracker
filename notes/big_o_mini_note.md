# Big-O Mini Note

O(1) = constant time / direct lookup  
Example: accessing `nums[0]`, dictionary lookup, set lookup

O(n) = one loop through the input  
Example: looping through `nums` once

O(n²) = nested loops  
Example: comparing every pair in brute force Two Sum or Contains Duplicate

O(log n) = cutting the search space in half  
Example: binary search

O(n log n) = common sorting complexity  
Example: Python `sorted()` usually takes O(n log n)

## My Problem Connections

Contains Duplicate brute force = O(n²)  
Contains Duplicate optimized = O(n)

Two Sum brute force = O(n²)  
Two Sum hashmap = O(n)

Best Time to Buy and Sell Stock brute force = O(n²)  
Best Time to Buy and Sell Stock optimized = O(n)

Merge Sorted Array using sorted() = O((m+n) log(m+n))

Maximum Subarray = O(n)