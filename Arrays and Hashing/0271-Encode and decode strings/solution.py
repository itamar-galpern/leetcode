"""
271. Encode and Decode Strings (Medium)
https://leetcode.com/problems/encode-and-decode-strings/
Solved 2026-08-28 | <15 min | unaided logic ; syntax help on join/f-string
Time O(n) / Space O(n)
Notes: notes.md
"""

def encode(strs: list[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    return ''.join(f"{len(w)}_{w}" for w in strs)
    

def decode(s: str) -> list[str]:
    """Decodes a single string to a list of strings.
    """
    i = 0
    return_list = []
    while i < len(s):
        # search for the delimiter
        j = i
        while s[j] != '_':
            j += 1
        # here we know s[j] = "_"
        length = int(s[i:j])
        return_list.append(s[j+1:j+1+length])
        i = j+length+1
    return return_list

if __name__ == "__main__":
    assert encode(["Hello", "World"]) == "5_Hello5_World"
    assert decode("5_Hello5_World") == ["Hello", "World"]
    assert encode([""]) == "0_"
    assert decode("0_") == [""]
    assert decode(encode(["_", "3_x", ""])) == ["_", "3_x", ""]
    print("ok")