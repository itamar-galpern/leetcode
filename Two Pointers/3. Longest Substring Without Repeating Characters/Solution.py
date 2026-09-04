"""
0003. Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Solved 2026-09-05 | <10 min | unaided
Time O(n) / Space O(n)
Notes: notes.md
"""


def lengthOfLongestSubstring(s: str) -> int:
    windows_chars = set()
    max_length = 0
    left_ptr, right_ptr = 0,0
    while right_ptr < len(s):
        curr_char = s[right_ptr]
        right_ptr += 1
        if curr_char in windows_chars:
            while s[left_ptr] != curr_char:
                windows_chars.remove(s[left_ptr])
                left_ptr += 1
            left_ptr += 1
        windows_chars.add(curr_char)
        curr_length = right_ptr - left_ptr
        if curr_length > max_length:
            max_length = curr_length
    return max_length
        
if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("") == 0
    assert lengthOfLongestSubstring(" ") == 1
    assert lengthOfLongestSubstring("au") == 2
    assert lengthOfLongestSubstring("dvdf") == 3
    print("ok")