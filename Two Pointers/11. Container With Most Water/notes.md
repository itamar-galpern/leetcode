# 011. Container With Most Water

**Trigger:** "max area between two lines" with an O(n) requirement -> two pointers starting at both ends, since the container's width only shrinks as pointers move inward — you should only ever move the pointer that can't possibly do better where it is.

**Approach:** Start pointers at both ends. At each step compute `min(height[left], height[right]) * (right - left)` and track the max. Move whichever pointer points at the shorter line inward — the taller one is never the bottleneck, so keeping it and shrinking width can only help by finding something taller on the other side.

**Where I lost time:** Moderate (~10 min) — likely spent convincing yourself that moving the shorter pointer (rather than always moving one side, or moving both) is provably correct and doesn't skip any potentially-better pairing.

**Complexity:** O(n) time, O(1) space.

**Redo:** no
