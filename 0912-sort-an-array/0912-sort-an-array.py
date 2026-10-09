class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        def rec_sort(nums):
            num_len = len(nums)
            if num_len <= 1:
                return nums
            else:
                left_sort = rec_sort(nums[:num_len//2])
                right_sort = rec_sort(nums[num_len//2:])
                sorted_return = []
                left, right = 0, 0
                len_left, len_right = len(left_sort), len(right_sort)
                while left < len_left or right < len_right:
                    if left >= len_left:
                        sorted_return.append(right_sort[right])
                        right += 1
                    elif right >= len_right:
                        sorted_return.append(left_sort[left])
                        left += 1
                    elif left_sort[left] < right_sort[right]:
                        sorted_return.append(left_sort[left])
                        left += 1
                    else:
                        sorted_return.append(right_sort[right])
                        right += 1
                return sorted_return
        return rec_sort(nums)