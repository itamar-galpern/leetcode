# 0167. Two Sum II - Input Array Is Sorted

**Trigger:** "two numbers summing to target, array is sorted" -> two pointers converging from both ends, since sortedness lets you decide which side to move from the sum vs. target comparison alone.

**Approach:** Start pointers at both ends. If the current sum is too small, move the left pointer right (increase the sum); if too large, move the right pointer left (decrease the sum); if equal, return the 1-indexed positions.

**Where I lost time:** Nowhere, immediate answer (<5 min) — likely straightforward off the back of having just done 3Sum's two-pointer core.

**Complexity:** O(n) time, O(1) space.

**Redo:** no
