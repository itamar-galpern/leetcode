# 0155. Min Stack

**Trigger:** "get the current minimum in O(1)" -> can't just track a single min variable (it wouldn't unwind correctly on pop), so keep a second, parallel stack that always reflects the minimum at each depth.

**Approach:** Maintain `stack` (all values) and `min_stack` (running minimums). On push, always push to `stack`; push to `min_stack` too only if it's empty or the new value is `<=` its current top (so ties are preserved for correct popping later). On pop, pop `stack`, and also pop `min_stack` if the popped value equals its current top. `getMin` is just `min_stack[-1]`.

**Where I lost time:** Nowhere, immediate answer (<5 min).

**Complexity:** O(1) time for every operation (push/pop/top/getMin), O(n) space for the two stacks.

**Redo:** no
