# DSA Tracker Next Features

## Current Tracker Status

My DSA Tracker currently supports:

- Add problem
- View all problems
- Delete problem
- Search problem
- Store data in JSON
- Store pattern
- Store time complexity
- Store space complexity
- Store note file path

The tracker now has my solved LeetCode problems with patterns, complexity, and notes.

---

## Next Feature 1: Total Solved Count

### Goal

Show the total number of solved problems.

### Idea

The tracker should count how many problem entries exist in `data.json`.

### Example Output

Total solved problems: 13

### Why this is useful

This will help me quickly see my overall progress.

---

## Next Feature 2: Difficulty Count

### Goal

Show how many Easy, Medium, and Hard problems I have solved.

### Example Output

Easy: 11  
Medium: 2  
Hard: 0

### Why this is useful

This helps me track whether I am only solving Easy problems or slowly moving toward Medium problems.

---

## Next Feature 3: Pattern Count

### Goal

Show how many problems I solved from each pattern.

### Example Output

HashMap: 4  
Two Pointers: 3  
Binary Search: 1  
Prefix/Suffix: 1  
Running Sum: 1

### Why this is useful

This will help me identify weak patterns and plan future practice.

---

## Next Feature 4: Filter by Difficulty

### Goal

Allow me to view only Easy, Medium, or Hard problems.

### Example

If I choose Medium, the tracker should only show Medium problems.

### Why this is useful

This will help when I want to review only Medium problems later.

---

## Next Feature 5: Filter by Pattern

### Goal

Allow me to view problems by pattern.

### Example

Search pattern: Binary Search

Output:
- Search Insert Position

### Why this is useful

This helps me review one DSA pattern at a time.

---

## Next Feature 6: Weekly Progress Summary

### Goal

Show how many problems I solved this week.

### Example Output

This week solved: 13 problems  
Notes written: 10 days  
GitHub pushed: Yes

### Why this is useful

This helps me stay consistent and measure weekly progress.

---

## Next Feature 7: Improve Menu Loop

### Current Problem

After choosing one menu option, the program sometimes exits.

### Goal

The tracker should return to the main menu after each action until I choose Exit.

### Why this is useful

This will make the tracker feel more like a real application.

---

## Priority Order

I should build the next features in this order:

1. Total solved count
2. Easy / Medium / Hard count
3. Pattern count
4. Improve menu loop
5. Filter by difficulty
6. Filter by pattern
7. Weekly progress summary

---

## Next Feature to Build

The next feature I should build is:

**Total Solved Count**

Reason:

This is simple, useful, and will help me practice working with `data.json` and list length.