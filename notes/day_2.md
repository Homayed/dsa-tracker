Day 2 Progress

Today I solved Valid Anagram and started understanding how dictionaries can be used to count frequency.

In the anagram problem, I first saw that two words can be anagrams if they have the same letters with the same number of appearances. This helped me understand that the main idea of the problem is not just comparing the words directly, but comparing the frequency of each character.

I learned that a dictionary stores data as key-value pairs. In this problem, the character became the key and the number of times it appeared became the value. For example, count["a"] = 3 means the letter "a" appears three times.

This problem helped me understand dictionary keys more clearly. I learned that when I write count[char], the current value of char becomes the key in the dictionary.

Main lessons:

An anagram is about same letters with same frequency.
Frequency means how many times something appears.
A dictionary stores data as key-value pairs.
In this problem, the key is the character and the value is the count.
count[char] means use the current character as the dictionary key.
Dictionaries are useful when I need to count things.

Pattern learned:
Character frequency counting

Project improvement:
Improved my understanding of dictionaries, which will help me build better features in my DSA Tracker.

code:

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counting = {}
        for c in s:
            if c not in counting:
                counting[c] = 1
            else:
                counting[c] += 1
        for c in t:
            if c not in counting:
                return False
            counting[c] -= 1


            
        for c in counting:
            if counting[c] != 0:
                return False
        return True


Pattern: Character frequency counting
Data structure: Dictionary / Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
Main idea: Count characters in s, subtract characters from t, then check if all counts become zero.