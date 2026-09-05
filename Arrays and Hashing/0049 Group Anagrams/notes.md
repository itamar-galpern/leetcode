# 0049. Group Anagrams

**Trigger:** "group strings that are anagrams of each other" -> need a canonical key that's identical for all anagrams of the same word -> sorted letters as a dict key.

**Approach:** For each word, sort its letters into a tuple (hashable) and use that as the key in a `defaultdict(list)`; append the original word to that key's bucket. Return all the buckets' values at the end.

**Where I lost time:** Nowhere, immediate answer (<5 min).

**Complexity:** O(n*k*log(k)) time and O(n*k) space, where n = number of words and k = max word length (dominated by sorting each word).

**Redo:** no
