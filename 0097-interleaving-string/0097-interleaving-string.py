class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[True for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

        for index_1 in range(len(s1)):
            if not (dp[index_1][0] and s1[index_1] == s3[index_1]):
                dp[index_1+1][0] = False
        for index_2 in range(len(s2)):
            if not (dp[0][index_2] and s2[index_2] == s3[index_2]):
                dp[0][index_2+1] = False

        for index_1 in range(1,len(s1)+1):
            for index_2 in range(1,len(s2)+1):
                from_s1 = dp[index_1-1][index_2] and s1[index_1-1] == s3[index_1+index_2-1]
                from_s2 = dp[index_1][index_2-1] and s2[index_2-1] == s3[index_1+index_2-1]
                dp[index_1][index_2] = from_s1 or from_s2
        return dp[len(s1)][len(s2)]

                