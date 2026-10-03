class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1] # dp[i] is the longest that includes i
        longest = 1
        for i in range(1,len(nums)):
            curr = nums[i]
            new_max = 0
            for j in range(i):
                candidate = nums[i-1-j]
                if curr > candidate:
                    if not new_max:
                        new_max = dp[i-1-j]
                    else:
                        new_max = max(new_max, dp[i-1-j])
            longest = max(longest, new_max+1)
            dp.append(new_max+1)
        return longest
            
                





        