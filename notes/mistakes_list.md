
# My Common DSA / Python Mistakes

## 1. Mixing up list index and dictionary key

I sometimes confuse list indexes with dictionary keys.

Example mistake:

```python
seen[i] = num
```

when the problem actually needs:

```python
seen[num] = i
```

Lesson:

```text
List index = position in a list
Dictionary key = lookup label/value
```

Example:

```text
Two Sum needs number → index
Contains Duplicate can use number → seen
```

---

## 2. Comparing a value with itself

In loops using `enumerate`, I sometimes forget that:

```python
for i, num in enumerate(nums):
```

means:

```text
num == nums[i]
```

So this kind of condition is useless:

```python
if num != nums[i]:
```

Lesson:

```text
num is already the value at nums[i].
```

---

## 3. Using nested loops first and getting TLE

I often start with brute force nested loops.

Examples:

```text
Contains Duplicate brute force
Two Sum brute force
Best Time to Buy and Sell Stock brute force
Product of Array Except Self brute force
```

Mistake:

```text
Nested loops often become O(n²), which can cause Time Limit Exceeded.
```

Lesson:

```text
Brute force is good for understanding, but then I must look for a better pattern.
```

---

## 4. Storing too much data

In Best Time to Buy and Sell Stock, I stored all profits in a list.

Mistake:

```python
profit.append(...)
```

This caused memory issues.

Lesson:

```text
Sometimes I do not need to store everything.
I only need the best value so far.
```

Example:

```text
Stock problem only needs max_profit and min_price.
Maximum Subarray only needs current_sum and max_sum.
```

---

## 5. Returning a new list when LeetCode wants in-place update

In problems like Move Zeroes, Merge Sorted Array, and Remove Element, I first tried to return a new list.

Mistake:

```python
return reformed_list
```

Lesson:

```text
If the problem says modify in-place, I must change the original list.
```

Correct idea:

```python
nums[:] = new_list
```

---

## 6. Forgetting what `nums[:]` means

I had to understand that:

```python
nums[:] = new_list
```

means:

```text
Replace the contents of the original list.
```

Lesson:

```text
nums = new_list changes the local variable.
nums[:] = new_list changes the original list LeetCode checks.
```

---

## 7. Using `pop()` wrongly

I thought:

```python
nums.pop(num)
```

would remove the value `num`.

But `pop()` removes by index, not value.

Lesson:

```text
pop(index) removes by position.
remove(value) removes by value.
```

Also, changing a list while looping through it can create confusing bugs.

---

## 8. Returning `True` too early

In Valid Anagram, I first wanted to return `True` when one character count became `0`.

Mistake:

```text
One character matching does not mean the whole string is an anagram.
```

Lesson:

```text
Count all characters.
Subtract all characters.
Only return True after checking every count is 0.
```

---

## 9. Forgetting length or final checks

In Valid Anagram, I needed to check all counts after subtracting.

In Remove Element, I needed to return the new length.

Lesson:

```text
Read the return requirement carefully.
Some problems ask for boolean.
Some ask for index.
Some ask for length.
Some ask to modify input only.
```

---

## 10. Trying to move `mid` directly in binary search

In Search Insert Position, I first tried to update `mid`.

Mistake:

```python
mid = mid / 2
mid = right - 1
mid = left + 1
```

Lesson:

```text
Do not move mid directly.
Move left or right.
Then recalculate mid.
```

Correct thinking:

```text
target < nums[mid] → move right
target > nums[mid] → move left
```

---

## 11. Using `target in nums` inside binary search

I tried:

```python
if target in nums:
```

inside binary search.

Mistake:

```text
target in nums scans the whole list and becomes O(n).
```

Lesson:

```text
Binary search should only compare with nums[mid].
```

---

## 12. Forgetting `return left` in Search Insert Position

For Search Insert Position, if the target is not found, I need to return `left`.

Lesson:

```text
After binary search ends, left becomes the correct insert position.
```

---

## 13. Confusing exact distance with “less than or equal to k”

In Contains Duplicate II, I first thought about checking only:

```text
i + k
```

Mistake:

```text
The problem says distance <= k, not exactly k.
```

Lesson:

```text
If duplicate indexes are within k distance, return True.
```

Correct idea:

```text
current index - previous index <= k
```

---

## 14. Forgetting to update dictionary with latest index

In Contains Duplicate II, the dictionary should store the latest index.

Lesson:

```text
seen[num] = i
```

means:

```text
Update this number’s latest position.
```

---

## 15. Confusing `price` and `prices`

In stock problem style loops:

```python
for i, price in enumerate(prices):
```

Mistake:

```python
price[j]
```

Lesson:

```text
price is one number.
prices is the full list.
```

---

## 16. Confusing `num` and `nums`

In binary/search problems:

```python
for num in nums:
```

Mistake:

```python
num[left]
```

Lesson:

```text
num is one value.
nums is the full list.
Only nums can be indexed.
```

---

## 17. Forgetting strings are immutable

I used:

```python
s.replace(" ", "")
```

but expected `s` to change.

Lesson:

```text
Strings do not change in-place.
replace() returns a new string.
```

Correct idea:

```python
s = s.replace(" ", "")
```

---

## 18. Thinking `ord(c) < 128` means letters only

In Valid Palindrome, I used ASCII checking and commas/spaces still appeared.

Lesson:

```text
ord(c) < 128 means ASCII, not letters only.
Commas and spaces are also ASCII.
```

Better idea:

```python
c.isalnum()
```

---

## 19. Forgetting lowercase conversion

In Valid Palindrome, uppercase and lowercase should be treated the same.

Lesson:

```text
Use lower() when comparing characters.
```

---

## 20. Using one shared count variable for character frequency

In Valid Anagram, I first tried one `count` variable for all characters.

Mistake:

```text
One count variable cannot track each character separately.
```

Lesson:

```text
Use dictionary values as counts.
seen[char] stores the count for that specific character.
```

---

## 21. Not knowing when to use prefix/suffix

In Product of Array Except Self, brute force caused TLE.

Lesson:

```text
When a problem asks for product/result except self, think:
left side result × right side result.
```

Pattern:

```text
Prefix / Suffix
```

---

## 22. Not understanding why `[1] * len(nums)` is used

In Product of Array Except Self, I learned:

```python
answer = [1] * len(nums)
```

creates an output container.

Lesson:

```text
Use 1 because multiplication starts from 1.
If I use 0, the product becomes 0.
```

---

## 23. Getting confused by reverse range

I had to understand:

```python
range(len(nums) - 1, -1, -1)
```

Lesson:

```text
Start from last index.
Move backward by 1.
Stop after index 0.
```

Example:

```text
For length 4 → 3, 2, 1, 0
```

---

## 24. Not always reading the exact requirement

Some problems want:

```text
return boolean
return index
return length
modify in-place
return list
```

Lesson:

```text
Before coding, I must ask:
What exactly does LeetCode want me to return or modify?
```

---

## 25. Pattern recognition is still developing

I am learning to identify clues:

```text
Duplicate / seen before → Set or HashMap
Anagram / frequency → Dictionary counting
Target sum → Complement lookup
Sorted array + search → Binary Search
Compare both ends → Two Pointers
Remove/move/modify in-place → In-place update
Maximum/best so far → Tracking / running sum
Before and after each index → Prefix/Suffix
```

Lesson:

```text
The problem statement gives clues.
The clues suggest the pattern.
The pattern suggests the data structure.
```

---

# Main Personal Lesson

My biggest recurring mistake is trying to code before fully identifying:

```text
1. What the problem is asking
2. What should be returned
3. Whether the input must be modified in-place
4. Which pattern fits the problem
5. What data structure is needed
```

My improvement rule:

```text
Before coding, I will write:
Pattern:
Data structure:
Return requirement:
Time complexity goal:
Main idea:
```