"""
238. Product of Array Except Self (Medium)
https://leetcode.com/problems/product-of-array-except-self/
Solved 2026-08-28 | <15 min | unaided
Time O(n) / Space O(n)
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    left_product = [1] * (n+1)
    right_product = [1] * (n+1)
    for i in range(n):
        left_product[i+1] = left_product[i] * nums[i]
        right_product[i+1] = right_product[i] * nums[n-i-1]
    return_array = [1] * n
    for i in range(n):
        return_array[i] = left_product[i] * right_product[n-i-1]
    return return_array
        

if __name__ == "__main__":
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
    assert productExceptSelf([0,0]) == [0,0]
    print("ok")