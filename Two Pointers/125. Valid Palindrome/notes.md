# 0125. Valid Palindrome

**Trigger:** "check if a string reads the same forwards/backwards, ignoring non-alphanumeric chars and case" -> two pointers converging from both ends, skipping non-alphanumeric characters as you go.

**Approach:** Start pointers at both ends. Before comparing, advance `left_ptr` past any non-alphanumeric character and retreat `right_ptr` past any non-alphanumeric character (each guarded by `left_ptr < right_ptr` so they don't cross). Compare the two characters case-insensitively; mismatch means not a palindrome. Move both pointers inward and repeat until they meet.

**Where I lost time:** Nowhere, immediate answer (<5 min).

**Complexity:** O(n) time, O(1) space.

**Redo:** no
