class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1] # dp[i] is the longest that includes i
        for i in range(1,len(nums)):
            curr = nums[i]
            new_max = 0
            for j in range(i):
                candidate = nums[i-1-j]
                if curr > candidate:
                    new_max = max(new_max, dp[i-1-j])
            dp.append(new_max+1)
        return max(dp)
            
                





        