from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        if not nums:
            return 0
        max_queue, min_queue = deque([0]), deque([0])
        # max, min are at index 0, we put indices inside
        max_length, left, right = 1, 0, 1
        while right < len(nums):
            candidate = nums[right]
            while max_queue and candidate >= nums[max_queue[-1]]:
                max_queue.pop()
            while min_queue and candidate <= nums[min_queue[-1]]:
                min_queue.pop()
            max_queue.append(right)
            min_queue.append(right)
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if max_queue[0] < min_queue[0]:
                    left = max_queue.popleft() + 1
                else:
                    left = min_queue.popleft() + 1
            right += 1
            max_length = max(max_length, right-left)
        return max_length
            
                    


        