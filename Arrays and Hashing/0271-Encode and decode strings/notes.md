# 271. Encode and Decode Strings

**Trigger:** "join/split a list of arbitrary strings reversibly" where strings may themselves contain the delimiter -> a self-describing (length-prefixed) format instead of a plain delimiter join.

**Approach:** Encode each string as `"{len(word)}_{word}"` and concatenate. To decode, scan forward from `i`, find the next `_`, parse the digits before it as the length, then slice exactly that many characters after the `_` as the next string; advance `i` past that slice and repeat.

**Where I lost time:** Logic came unaided; the ~15 min was mostly Python syntax — getting comfortable with the generator-expression + f-string combo inside `''.join(...)` (as noted in the file header), not the encoding scheme itself.

**Complexity:** O(n) time and space, where n = total characters across all strings (each char is read/written once).

**Redo:** no
