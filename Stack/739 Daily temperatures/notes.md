# 0739. Daily Temperatures

**Trigger:** "next warmer day for each index" -> classic "next greater element" pattern -> monotonic decreasing stack of (value, index).

**Approach:** Walk temperatures with their index. While the stack's top temperature is colder than the current one, pop it and fill in its answer as `current_index - popped_index` (days waited). Push the current `(temp, i)` onto the stack. Anything left on the stack at the end never finds a warmer day and keeps its default 0.

**Where I lost time:** Most of the ~20 min was likely spent arriving at the monotonic-stack pattern itself (vs. a naive O(n^2) scan) and deciding to store `(temp, idx)` pairs so the distance can be recovered on resolution.

**Complexity:** O(n) time (each index is pushed and popped at most once), O(n) space for the stack and result array.

**Redo:** no
