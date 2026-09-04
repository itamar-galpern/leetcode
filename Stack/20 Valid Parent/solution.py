
"""
0020. Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/
Solved 2026-08-31 | <5 min | unaided
Time O(n) / Space O(n)
Notes: notes.md
"""

def isValid(s: str) -> bool:
    curr_stack = list()
    bracket_dictionary = {'}' : '{', ')' : '(', ']' : '['}
    for bracket in s:
        if bracket in bracket_dictionary.values():
            curr_stack.append(bracket)
        else:
            if not curr_stack:
                return False
            curr = curr_stack.pop()
            if bracket_dictionary[bracket] != curr:
                return False
    if not curr_stack:
        return True
    return False

if __name__ == "__main__":
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("([)]") == False
    assert isValid("{[]}") == True
    print("ok")