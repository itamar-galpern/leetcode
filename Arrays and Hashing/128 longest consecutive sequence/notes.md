# 0128. Longest Consecutive Sequence

**Trigger:** "longest run of consecutive integers, O(n) required" -> hash set for O(1) membership, but only start counting a run from its true start (`num-1` not in the set) so each number is visited O(1) amortized times total.

**Approach:** Put all numbers in a set. For each number, skip it if `num-1` is in the set (it's not a sequence start). Otherwise walk forward (`num+1`, `num+2`, ...) counting how long the consecutive run is, and track the max.

**Where I lost time:** Most of the ~20 min was likely spent arriving at the "only start from a sequence-start" trick — the naive version (checking `num+1` from every number) is the obvious first idea but degrades to O(n^2) on a fully consecutive input, so getting to the O(n) insight takes a beat.

**Complexity:** O(n) time (each element is visited at most twice — once as a skip check, once as part of exactly one run), O(n) space for the set.

**Redo:** no
