"""
0015. 3Sum (Medium)
https://leetcode.com/problems/3sum/
Solved 2026-09-02 | <15 min | unaided
Time O(n^2) / Space O(n^2)
Notes: notes.md
"""


def threeSum(nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result_arr = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left_ptr = i+1
            right_ptr = n-1
            target = - nums[i]
            while left_ptr < right_ptr:
                sum = nums[left_ptr] + nums[right_ptr]
                if sum < target:
                    left_ptr += 1
                elif sum > target:
                    right_ptr -= 1
                else:
                    result_arr.append([nums[i], nums[left_ptr], nums[right_ptr]])
                    left_ptr += 1
                    right_ptr -= 1
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr-1]:
                        left_ptr += 1
        return result_arr

        
if __name__ == "__main__":
    assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert threeSum([0,1,1]) == []
    assert threeSum([0,0,0]) == [[0,0,0]]
    assert threeSum([-2,0,1,1,2]) == [[-2,0,2],[-2,1,1]]
    print("ok")

    