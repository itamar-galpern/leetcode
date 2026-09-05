"""
0128. Longest Consecutive Sequence (Medium)
https://leetcode.com/problems/longest-consecutive-sequence/
Solved 2026-08-28 | <20 min | unaided
Time O(n) / Space O(n)
"""

def longestConsecutive(nums: list[int]) -> int:
        max_length = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 in num_set:
                continue
            curr_length = 0
            curr = num
            while curr in num_set:
                curr = curr+1
                curr_length += 1
            max_length = max(max_length, curr_length)
        return max_length

if __name__ == "__main__":
    assert longestConsecutive([100,4,200,1,3,2]) == 4
    assert longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7]) == 4
    print("ok")