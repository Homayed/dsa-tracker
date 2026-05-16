Today I solved Two Sum and started understanding the hash map lookup pattern.

In the Two Sum problem, I first understood the brute force approach: compare every number with every other number and check if their sum equals the target. This helped me understand the problem clearly, but the brute force approach is slow because it uses nested loops.

Then I learned the better way of thinking: for every current number, ask what number I need to reach the target. This needed number is called the complement.

For example, if the target is 9 and the current number is 7, then the needed number is 2. If I have already seen 2, then I found the answer.

I learned that in Two Sum, the dictionary stores the number as the key and the index as the value. For example, seen[2] = 0 means the number 2 is located at index 0.

Main lessons:

Two Sum asks for indexes, not the actual numbers.
Brute force checks every pair and causes O(n²) time.
A dictionary can help me remember previous numbers.
In this problem, the key is the number and the value is the index.
seen[needed] gives the index of the number I need.
Hash map lookup helps reduce repeated searching.

Pattern learned:
Complement lookup

Project improvement:
Strengthened my dictionary understanding and became more confident with key-value logic.

Code:

seen = {}

for i, num in enumerate(nums):
    required = target - num

    if required in seen:
        return [seen[required], i]

    seen[num] = i

Pattern: Complement lookup
Data structure: Dictionary / Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
Main idea: For each number, calculate required = target - num. If the required number already exists in the dictionary, return its saved index and the current index. Then store the current number with its index.