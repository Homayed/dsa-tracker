# Valid Anagram Review

Pattern:
Hash Map / Frequency Counting

Main idea:
Two strings are anagrams if they have the same characters with the same frequency.

Steps:
1. Check if lengths are different.
2. Count characters in the first string.
3. Count characters in the second string.
4. Compare both dictionaries.

Why dictionary:
Dictionary stores each character as a key and its frequency as the value.

Time Complexity:
O(n)

Space Complexity:
O(1) if only lowercase English letters, otherwise O(n)

Mistake to remember:
Do not only check if letters exist. The frequency must also match.