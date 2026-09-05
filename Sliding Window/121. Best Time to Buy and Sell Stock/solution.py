"""
0121. Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Solved 2026-09-05 | <10 min | unaided
Time O(n) / Space O(1)
"""


def maxProfit(prices: list[int]) -> int:
    left_ptr, right_ptr = 0, 0
    max_profit = 0
    if not prices:
        raise ValueError("Invalid input")
    while right_ptr < len(prices)-1:
        if prices[left_ptr] >= prices[right_ptr]:
            left_ptr = right_ptr
        right_ptr += 1
        curr_profit = prices[right_ptr] - prices[left_ptr]
        if curr_profit > max_profit:
            max_profit = curr_profit
    if max_profit <= 0:
        return 0
    return max_profit

if __name__ == "__main__":
    assert maxProfit([7,1,5,3,6,4]) == 5
    assert maxProfit([7,6,4,3,1]) == 0
    assert maxProfit([1,2]) == 1
    assert maxProfit([2,1]) == 0
    assert maxProfit([1]) == 0
    print("ok")

    