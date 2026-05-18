# Day 11 Progress

Today I solved Group Anagrams.

## Problem: Group Anagrams

Pattern: HashMap / Grouping by key  
Data structure: Dictionary  
Time Complexity: O(n * k log k)  
Space Complexity: O(n * k)

Main idea:
Words that are anagrams should produce the same key. I used the sorted version of each word as the key.

Example:
"eat", "tea", and "ate" all become "aet", so they go into the same group.

## What I learned

For grouping problems, I should think:

key -> list of matching values

In this problem:
sorted word -> list of original words

## Mistake I made

At first, I used the index or the sorted word itself as the value. Then I understood that the dictionary value should be a list of original words.

## Final lesson

When multiple items belong together, use a dictionary where each key maps to a list.