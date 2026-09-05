"""
0125. Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome/
Solved 2026-09-05 | <5 min | unaided
Time O(n) / Space O(1)
"""

def isPalindrome(s: str) -> bool:
    left_ptr, right_ptr = 0, len(s) -1
    while left_ptr < right_ptr:
        while left_ptr < right_ptr and not s[left_ptr].isalnum():
            left_ptr += 1
        while left_ptr < right_ptr and not s[right_ptr].isalnum():
            right_ptr -= 1
        if s[left_ptr].lower() != s[right_ptr].lower():
            return False
        left_ptr += 1
        right_ptr -= 1
    return True

if __name__ == "__main__":
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome(" ") == True
    assert isPalindrome("0P") == False
    assert isPalindrome("ab_a") == True
    print("ok")
    