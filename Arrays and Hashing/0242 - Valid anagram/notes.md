# 242. Valid Anagram

**Trigger:** "do two strings have the same letters with the same frequency" -> fixed-size counting array indexed by letter, since input is lowercase a-z.

**Approach:** Early-exit if lengths differ. Use a 26-length count array, incrementing per letter of `s` and decrementing per letter of `t` in the same pass structure; if any count goes negative while processing `t`, `t` has a letter `s` doesn't (or too many of it), so return False immediately. If nothing goes negative, they're anagrams.

**Where I lost time:** Nowhere, immediate answer (<3 min).

**Complexity:** O(n) time, O(1) space (fixed 26-slot array regardless of input size).

**Redo:** no
