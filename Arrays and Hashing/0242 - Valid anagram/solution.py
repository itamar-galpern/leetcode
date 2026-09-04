"""
242. Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/
Solved 2026-08-28 | <3 min | unaided
Time O(n) / Space O(1)
Notes: notes.md
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for letter in s:
        count[ord(letter)-ord('a')] += 1
    for letter in t:
        count[ord(letter)-ord('a')] -= 1
        if (count[ord(letter)-ord('a')] < 0):
            return False
    return True


if __name__ == "__main__":
    assert isAnagram("anagram", "nagaram") is True
    assert isAnagram("rat", "car") is False
    assert isAnagram("", "") is True
    print("ok")
