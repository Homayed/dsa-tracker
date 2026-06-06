# Contains Duplicate Review

Pattern:
Hash Map / Set-style lookup

Main idea:
I do not need to count every number. I only need to check if I have seen the number before.

Steps:
1. Create an empty dictionary.
2. Loop through nums.
3. If num is already in dictionary, return True.
4. Otherwise, store num in dictionary.
5. If the loop finishes, return False.

Why this is better than counting:
It stops immediately when a duplicate is found.

Time Complexity: O(n)
Space Complexity: O(n)