Day 4 Progress

Today I solved Best Time to Buy and Sell Stock and added the search function to my DSA Tracker project.

In the stock problem, I first tried to compare every buying day with every selling day. This helped me understand the brute force approach, but it caused time limit issues because it used nested loops. Then I learned that I only need to track the lowest price so far and the maximum profit so far. This is called one-pass tracking.

In my DSA Tracker, I built a search function by loading the saved JSON data, looping through each problem dictionary, checking the "problem" key, and comparing it with the user’s search input. I also learned how to use a found variable to show a message when no matching problem is found.

Main lessons:
- Nested loops can cause Time Limit Exceeded.
- Storing every profit can cause Memory Limit Exceeded.
- Some problems only require tracking the best value so far.
- In dictionaries, "problem" in item checks if a key exists.
- item["problem"] gets the saved problem name.

Pattern learned:
One-pass tracking

Project improvement:
Search problem feature added to DSA Tracker