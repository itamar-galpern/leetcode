class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return True
        furthest = 0
        for i, jump in enumerate(nums):
            if i > furthest:
                return False
            furthest = max(furthest, i+jump)
            if furthest >= len(nums)-1:
                return True


        