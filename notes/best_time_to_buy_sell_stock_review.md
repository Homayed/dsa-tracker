# Best Time to Buy and Sell Stock Review

Pattern:
Two Pointers / One Pass Tracking

Main idea:
left is the buy day.
right is the sell day.
If selling today gives profit, update max_profit.
If today’s price is lower than the buy price, make today the new buy day.

Mistake to remember:
right must move forward every loop.
When a lower price is found, use left = right, not left += 1.

Time Complexity: O(n)
Space Complexity: O(1)