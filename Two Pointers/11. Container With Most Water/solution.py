"""
011. Container With Most Water (Medium)
https://leetcode.com/problems/container-with-most-water/
Solved 2026-09-05 | <10 min | unaided
Time O(n) / Space O(1)
"""


def maxArea(height: list[int]) -> int:
    left, right = 0, len(height)-1
    max_result = 0
    while left < right:
        left_height, right_height = height[left], height[right]
        min_height = min(left_height, right_height)
        distance = right - left
        if min_height * distance > max_result:
            max_result = min_height * distance
        if left_height < right_height:
            left += 1
        else:
            right -= 1
    return max_result

if __name__ == "__main__":
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([1,1]) == 1
    assert maxArea([4,3,2,1,4]) == 16
    assert maxArea([1,2,1]) == 2
    print("ok")
    