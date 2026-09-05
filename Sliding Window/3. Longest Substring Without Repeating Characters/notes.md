# 0003. Longest Substring Without Repeating Characters

**Trigger:** "longest substring with no repeated characters" -> sliding window: grow the right edge, and when a duplicate is found, shrink the left edge just enough to remove it, tracking membership with a set.

**Approach:** Expand `right_ptr`, adding each new character to `windows_chars`. If the incoming character is already in the window, shrink from `left_ptr` — removing characters from the set and advancing `left_ptr` — until the earlier occurrence of that character is removed, then step past it. Add the current character to the set and update `max_length` with the current window size (`right_ptr - left_ptr`).

**Where I lost time:** Moderate (~10 min) — the inner shrink-loop (advancing `left_ptr` exactly up to and past the duplicate's earlier occurrence, then still adding the current char afterward) is the part most likely to need a couple of tries to get the boundaries right.

**Complexity:** O(n) time (each character is added and removed from the set at most once), O(min(n, charset size)) space for the set (commonly stated as O(n)).

**Redo:** no
