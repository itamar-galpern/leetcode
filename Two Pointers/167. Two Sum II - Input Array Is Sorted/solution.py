"""
0121. Two Sum II - Input Array Is Sorted (Easy)
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Solved 2026-09-01 | <5 min | unaided
Time O(n) / Space O(1)
"""


def twoSum(numbers: list[int], target: int) -> list[int]:
    left_ptr, right_ptr = 0, len(numbers) -1
    while left_ptr < right_ptr:
        sum = numbers[left_ptr] +numbers[right_ptr]
        if sum < target:
            left_ptr += 1
        elif sum > target:
            right_ptr -= 1
        else:
            return [left_ptr+1, right_ptr+1]
    raise ValueError("No solution found")
            

if __name__ == "__main__":
    assert twoSum([2,7,11,15], 9) == [1,2]
    assert twoSum([2,3,4], 6) == [1,3]
    assert twoSum([-1,0], -1) == [1,2]
    print("ok")