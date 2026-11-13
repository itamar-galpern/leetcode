class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        count = 0
        for i in range(len(s)):
            if s[i] == 'b':
                count += 1
                dp[i+1] = dp[i]
            else:
                dp[i+1] = min(dp[i]+1,count)
        return dp[-1]