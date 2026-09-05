"""
0567. Permutation in String (Medium)
https://leetcode.com/problems/permutation-in-string/
Solved 2026-09-05 | <10 min | unaided
Time O(n) / Space O(1)
"""

def checkInclusion(s1: str, s2: str) -> bool:
    s1_code = [0] * 26
    temp_code = [0] * 26
    s1_length = len(s1)
    if s1_length > len(s2):
        return False
    for i in range(s1_length):
        s1_code[ord(s1[i]) - ord('a')] += 1
        temp_code[ord(s2[i]) - ord('a')] += 1
    if temp_code == s1_code:
        return True
    right_ptr = s1_length
    while right_ptr < len(s2):
        temp_code[ord(s2[right_ptr-s1_length])-ord('a')] -= 1
        temp_code[ord(s2[right_ptr])-ord('a')] += 1
        if temp_code == s1_code:
            return True
        right_ptr += 1
    return False

if __name__ == "__main__":
    assert checkInclusion("ab", "eidbaooo") == True
    assert checkInclusion("ab", "eidboaoo") == False
    assert checkInclusion("adc", "dcda") == True
    assert checkInclusion("hello", "ooolleoooleh") == False
    print("ok")