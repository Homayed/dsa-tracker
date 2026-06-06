Optimized approach:
Use two pointers directly on the original string.

Main idea:
Left pointer starts at the beginning.
Right pointer starts at the end.
Skip non-alphanumeric characters.
Compare lowercase characters.
If mismatch happens, return False.
If pointers cross, return True.

Time Complexity: O(n)
Space Complexity: O(1)

Why O(1) space:
I do not create a cleaned string or list. I only use left and right pointers.