# Day 5 Progress

Today I solved **Valid Palindrome** and learned the **Two Pointers** pattern.

In this problem, I first understood that a valid palindrome should read the same from left to right and right to left. However, the input string can contain uppercase letters, spaces, commas, colons, and other non-alphanumeric characters. So before checking the palindrome, I needed to clean the string.

I built a cleaned version of the string by keeping only letters and numbers using `isalnum()`, and converting every character to lowercase using `lower()`. This helped me understand how to prepare messy input before applying the main logic.

After cleaning the string, I used two pointers: one pointer starting from the left side and another pointer starting from the right side. Then I compared both characters. If they were different, I returned `False`. If they matched, I moved both pointers toward the middle. If the loop finished without finding a mismatch, I returned `True`.

Main lessons:

* A palindrome reads the same forward and backward.
* `isalnum()` checks whether a character is a letter or number.
* `lower()` helps make uppercase and lowercase letters equal.
* Cleaning input can make the main problem easier.
* Two pointers are useful when comparing values from both ends.
* `left` starts at the beginning and `right` starts at the end.
* If `cleaned[left] != cleaned[right]`, the string is not a palindrome.
* If all comparisons match, the string is a valid palindrome.
* `return` stops the function, so `break` is not needed after `return`.

Pattern learned:
Two Pointers

Project improvement:
Added **Valid Palindrome** to the DSA Tracker, bringing the total tracked solved problems to **5**.

Big-O understanding:

* Cleaning the string takes `O(n)` time.
* The two-pointer check also takes `O(n)` time.
* Total time complexity is `O(n)`.
* Space complexity is `O(n)` because I created a new cleaned string.

Reflection:
Today I understood that not every problem should be solved directly on the original input. Sometimes I need to clean or prepare the data first. I also learned how two pointers work by comparing characters from both sides of a string. This problem helped me become more comfortable with string processing, loops, indexes, and pointer movement.
