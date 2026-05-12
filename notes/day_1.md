Day 1 Progress

Today I solved Contains Duplicate and started understanding how sets can be used to detect repeated values.

In the duplicate problem, I first thought about comparing every number with every other number. This helped me understand the brute force approach, but it caused time limit issues because it used nested loops. Then I learned that I do not need to compare every pair. I only need to remember which numbers I have already seen.

I learned that a set is useful when I want to check whether something already exists. In this problem, the set helped me ask one simple question: have I seen this number before? If the answer is yes, then the list contains a duplicate.

Main lessons:

Brute force means trying every possible comparison.
Nested loops can cause Time Limit Exceeded.
A set stores unique values only.
A set is useful for checking if something has already appeared.
I do not always need to store all values in a list.
Sometimes I only need to remember what I have already seen.

Pattern learned:
Seen-before checking

Project improvement:
Started building consistency with LeetCode and began connecting DSA problems with my tracker project.