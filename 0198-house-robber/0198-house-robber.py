class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0, nums[0]] # dp[i] = max money nums[:i]
        for i in range(1,len(nums)):
            new_max = max(dp[i-1]+nums[i], dp[i])
            dp.append(new_max)
        return dp[-1]

            
        