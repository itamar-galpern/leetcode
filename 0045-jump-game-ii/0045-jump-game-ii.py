class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        i, steps = 0, 0
        while i < len(nums):
            steps += 1
            jump_range = nums[i]
            best_index, furthest = i, i+jump_range
            for jump in range(1,jump_range+1):
                key = i + jump
                if key == len(nums)-1:
                    return steps
                candidate = nums[key]
                if candidate+key >= furthest:
                    best_index, furthest = key, candidate+key
            i = best_index
        return steps
                
                
                