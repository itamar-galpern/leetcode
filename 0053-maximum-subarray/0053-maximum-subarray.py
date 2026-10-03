class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return None
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = max(0,curr_sum) + num
            max_sum = max(curr_sum, max_sum)
        return max_sum
        