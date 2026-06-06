# Two Sum Review

Pattern: Hash Map / Dictionary

Main idea:
For each number, calculate the needed number:
needed = target - num

If needed already exists in the dictionary, return:
index of needed number and current index.

If not found, store:
current number -> current index

Why dictionary:
Dictionary helps check the needed number quickly.

Time Complexity: O(n)
Space Complexity: O(n)

Mistake to remember:
Return dic[needed], not dic[num].