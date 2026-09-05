# 0347. Top K Frequent Elements

**⚠ Flag:** `solution.py` currently contains the `encode`/`decode` string functions copy-pasted from problem 271, not a Top K Frequent Elements solution. There's no `topKFrequent` function and no matching test block. This file needs to actually be (re)written before these notes can reflect a real approach.

**Trigger:** "k most frequent elements" -> count frequencies, then avoid a full sort by bucketing counts (bucket index = frequency, capped at n) and reading buckets from the high end.

**Approach:** *(not yet implemented in solution.py — to fill in once written)* Typically: build a frequency map with `Counter`/`defaultdict(int)`, create `n+1` buckets indexed by frequency, place each number in `buckets[freq]`, then walk buckets from `n` down to `1` collecting numbers until k are gathered.

**Where I lost time:** N/A — solution not actually written yet.

**Complexity:** Bucket-sort approach: O(n) time, O(n) space. (The current file's declared "O(n)/O(n)" describes the encode/decode logic actually present, not this problem.)

**Redo:** no
