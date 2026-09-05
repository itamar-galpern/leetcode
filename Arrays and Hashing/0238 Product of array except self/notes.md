# 238. Product of Array Except Self

**Trigger:** "product of every element except self, no division" -> prefix product from the left and suffix product from the right, combine at each index.

**Approach:** Build `left_product` where `left_product[i+1]` = product of everything left of index i, and `right_product` where `right_product[i+1]` = product of everything right of index `n-i-1` (built by walking left-to-right but indexing from the array's other end). Both arrays are padded to size n+1 so index 0 is the identity (1). The answer at index i is `left_product[i] * right_product[n-i-1]`.

**Where I lost time:** Most of the ~15 min likely went into the off-by-one/mirrored indexing — padding both arrays by 1 and figuring out that `right_product` needs to be read from `n-i-1` to line up with `left_product[i]` is the fiddly part of this pattern.

**Complexity:** O(n) time, O(n) space (two auxiliary arrays; could be reduced to O(1) extra space by building the output array in place and folding the second pass into it).

**Redo:** no
