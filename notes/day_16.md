# Day 16 — Longest Substring Without Repeating Characters, Sliding Window, and Tracker Topic Count

## Date
25 May 2026

## Main Focus

Today I completed my first proper Sliding Window problem and added another useful feature to my DSA Tracker.

Main work completed:

- Longest Substring Without Repeating Characters
- First official Sliding Window pattern
- Variable-size Sliding Window + Hash Set
- Added problem to DSA Tracker
- Added Count by Topic feature to tracker
- Fixed GitHub authentication issue
- Successfully pushed latest tracker updates to GitHub

---

# 1. Roadmap Status

Today matches the roadmap’s Day 26-style task:

- Longest Substring Without Repeating Characters
- Valid Parentheses review
- Tracker feature improvement
- GitHub push

I already solved Valid Parentheses before, so today’s main new problem was Longest Substring Without Repeating Characters.

---

# 2. Problem Completed Today — Longest Substring Without Repeating Characters

## Problem

Given a string `s`, return the length of the longest substring without repeating characters.

Example:

```python
s = "abcabcbb"
```

The longest substring without repeating characters is:

```text
"abc"
```

Answer:

```python
3
```

---

## Topic

Sliding Window

## Pattern

Variable-size Sliding Window + Hash Set

---

# 3. Why This Is Sliding Window

This is my first proper Sliding Window problem.

The window is a section of the string.

Example:

```text
s = "abcabcbb"

window = "abc"
```

The rule is:

```text
The window must not contain duplicate characters.
```

If a duplicate appears, the window becomes invalid.

So:

```text
right pointer expands the window
left pointer shrinks the window
set checks if the window has duplicate characters
```

---

# 4. Main Idea

Use a set to store the characters currently inside the window.

```python
char_set = set()
```

Use two pointers:

```python
left = 0
right = moves through the string
```

For every `right` character:

```text
If s[right] is already in the set:
    remove characters from the left until duplicate is gone

Then:
    add s[right]
    update max length
```

---

# 5. Important Line

```python
while s[right] in char_set:
    char_set.remove(s[left])
    left += 1
```

Meaning:

```text
While the new character already exists in my window,
remove characters from the left side until the window becomes valid again.
```

Then:

```python
char_set.add(s[right])
```

Meaning:

```text
Now add the new character into the clean window.
```

---

# 6. Window Length Formula

```python
current_length = right - left + 1
```

This means:

```text
Current window size = right index - left index + 1
```

Example:

```text
s = "abcabcbb"

left = 0
right = 2

window = "abc"
indexes = 0, 1, 2
```

Length:

```python
2 - 0 + 1 = 3
```

The `+1` is needed because both `left` and `right` positions are included.

Memory:

```text
Window length = right - left + 1
```

---

# 7. Final Code

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_count = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            current_length = right - left + 1

            if current_length > max_count:
                max_count = current_length

        return max_count
```

---

# 8. Dry Run

Example:

```python
s = "abcabcbb"
```

Start:

```text
left = 0
char_set = {}
max_count = 0
```

Read `"a"`:

```text
char_set = {a}
window = "a"
current_length = 1
max_count = 1
```

Read `"b"`:

```text
char_set = {a, b}
window = "ab"
current_length = 2
max_count = 2
```

Read `"c"`:

```text
char_set = {a, b, c}
window = "abc"
current_length = 3
max_count = 3
```

Read next `"a"`:

```text
"a" is already in char_set
remove s[left] = "a"
left moves to 1
now add new "a"
window = "bca"
max_count stays 3
```

Final answer:

```python
3
```

---

# 9. Complexity

```text
Time Complexity: O(n)
Space Complexity: O(n)
```

Reason:

Each character is added and removed from the set at most once.

The set may store up to `n` characters in the worst case.

---

# 10. What I Learned

```text
Sliding Window means keeping a valid section of the string or array.
right expands the window.
left shrinks the window when the window becomes invalid.
A set helps detect duplicate characters.
```

Main memory line:

```text
Duplicate found -> shrink from left.
No duplicate -> expand right.
```

---

# 11. DSA Tracker Entry

I added this problem to my DSA Tracker.

```text
Problem name: Longest Substring Without Repeating Characters
Difficulty: Medium
Topic: Sliding Window
Pattern: Variable-size Sliding Window + Hash Set
Time Complexity: O(n)
Space Complexity: O(n)
Note file: notes/day_16.md
Status: Completed
```

---

# 12. Tracker Feature Added — Count by Topic

Today I also added a new DSA Tracker feature:

```text
Count By Topic
```

## Purpose

The feature shows how many solved problems I have from each DSA topic.

Example output:

```text
Arrays & Hashing: 8
Two Pointers: 4
Stack: 3
Sliding Window: 1
```

This helps me understand which topics I am strong in and which topics need more work.

---

## Feature Code

```python
def count_by_topic():
    data = load_data()

    if not data:
        print("\nNo problems found.\n")
        return

    topic_count = {}

    for problem in data:
        topic = problem.get("topic", "Unknown").strip()

        if topic == "":
            topic = "Unknown"

        if topic not in topic_count:
            topic_count[topic] = 1
        else:
            topic_count[topic] += 1

    print("\n===== Problems Count By Topic =====")

    for topic, count in topic_count.items():
        print(f"{topic}: {count}")

    print("===================================\n")
```

---

## What I Learned From This Feature

```text
Use a dictionary to count repeated topics.
Each topic becomes a key.
The count becomes the value.
```

Example:

```python
topic_count = {
    "Two Pointers": 4,
    "Stack": 3,
    "Sliding Window": 1
}
```

This is the same basic idea as frequency counting in problems like Top K Frequent Elements.

---

# 13. GitHub Push

I fixed the GitHub authentication issue and successfully pushed the latest changes.

Successful push message:

```text
main -> main
```

Completed:

```text
Longest Substring added
Count by Topic feature added
Tracker updated
GitHub pushed
```

---

# 14. Review Notes

## Sliding Window vs Two Pointers

I have done Two Pointers before:

```text
Two Sum II
3Sum
Container With Most Water
Valid Palindrome
```

But Longest Substring Without Repeating Characters is different.

Two Pointers:

```text
Usually left and right move toward each other or scan based on a fixed condition.
```

Sliding Window:

```text
left and right create a window.
right expands.
left shrinks when the window becomes invalid.
```

For this problem:

```text
Valid window = no repeated characters
Invalid window = duplicate character appears
```

---

# 15. Weak Areas To Review

```text
Sliding Window dry runs
Why current_length = right - left + 1
When to use while instead of if
How the set changes when duplicates appear
```

---

# 16. Current Progress

Completed today:

```text
Longest Substring Without Repeating Characters ✅
First Sliding Window problem ✅
Added to DSA Tracker ✅
Count by Topic feature ✅
GitHub push ✅
```

Current patterns learned so far:

```text
Arrays & Hashing
Hash Map
Hash Set
Two Pointers
Stack
Heap
Sliding Window
```

---

# 17. Next Step

Next roadmap task:

```text
Day 27 — Course review / weekly review
```

Focus:

```text
Review CU Boulder Module 2
Review recent LeetCode problems
Check tracker stats
Plan next roadmap steps
```

Recent problems to review:

```text
3Sum
Container With Most Water
Longest Substring Without Repeating Characters
Valid Parentheses
Min Stack
Top K Frequent Elements
```

---

# Final Reflection

Today was important because I started a new pattern: Sliding Window.

I now understand that Sliding Window is about keeping a valid section of the string or array.

The main lesson:

```text
right expands the window.
left shrinks the window.
set keeps the window clean.
```

I also improved my DSA Tracker by adding Count by Topic, which makes the project more useful and better for GitHub/MLH preparation.