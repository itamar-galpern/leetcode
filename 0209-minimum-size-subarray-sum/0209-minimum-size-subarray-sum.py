class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, right = 0, 0
        min_length = math.inf
        current_sum = 0
        while right < len(nums):
            current_sum += nums[right]
            if current_sum >= target:
                while current_sum >= target:
                    current_sum -= nums[left]
                    left += 1
                min_length = min(min_length, right-left+2)
            right += 1
        return min_length if min_length != math.inf else 0
        