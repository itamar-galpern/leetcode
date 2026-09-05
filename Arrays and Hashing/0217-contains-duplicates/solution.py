"""
217. Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/
Solved 2026-08-28 | <1 min | unaided
Time O(n) / Space O(n)
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
    print("ok")
