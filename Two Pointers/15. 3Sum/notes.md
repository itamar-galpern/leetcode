# 0015. 3Sum

**Trigger:** "triplets summing to zero, no duplicates" -> sort first (enables both an early-exit and easy duplicate skipping), fix one element, then two-pointer scan for the other two.

**Approach:** Sort `nums`. For each index `i` as the fixed first element (break early once `nums[i] > 0` since nothing after can bring the sum back to 0; skip `i` if it's the same value as the previous one to avoid duplicate triplets), run a two-pointer scan over the remaining range for a pair summing to `-nums[i]`. On a match, record the triplet and advance both pointers, also skipping past any duplicate value on the left pointer before continuing.

**Where I lost time:** Most of the ~15 min was likely the duplicate-skipping logic — getting both the outer-loop skip (`nums[i] == nums[i-1]`) and the inner left-pointer skip after a match right, without accidentally skipping a valid triplet.

**Complexity:** O(n^2) time (sort is O(n log n), dominated by the O(n) outer loop x O(n) two-pointer scan), O(n^2) space if counting the worst-case output size (O(log n) or O(n) if only counting the sort's/auxiliary space).

**Redo:** no
