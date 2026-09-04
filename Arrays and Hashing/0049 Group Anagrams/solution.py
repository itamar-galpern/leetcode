"""
0049. Group Anagrams (Medium)
https://leetcode.com/problems/group-anagrams/
Solved 2026-08-28 | <5 min | unaided
Time O(n*k*log(k)) / Space O(n*k) where n = len(strs) and k = max(len(word) for word in strs)
Notes: notes.md
"""
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        anagram_groups[key].append(word)
    return list(anagram_groups.values())
        

if __name__ == "__main__":
    assert groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert groupAnagrams([""]) == [[""]]
    assert groupAnagrams(["a"]) == [["a"]]
    print("ok")