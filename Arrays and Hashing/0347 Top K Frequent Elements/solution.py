"""
0347. Top K Frequent Elements (Medium)
https://leetcode.com/problems/top-k-frequent-elements/
Solved 2026-08-28 | <10 min | unaided
Time O(n) / Space O(n)
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
        j = i
        while s[j] != '_':
            j += 1
        length = int(s[i:j])
        return_list.append(s[j+1:j+1+length])
        i = j+length+1
    return return_list




            
if __name__ == "__main__":
    assert encode(["hello", "world"]) == "5_hello5_world"
    assert decode("5_hello5_world") == ["hello", "world"]
    assert encode([]) == ""
    assert decode("") == []
    print("ok")