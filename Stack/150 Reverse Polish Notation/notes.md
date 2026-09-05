# 0150. Evaluate Reverse Polish Notation

**Trigger:** "postfix expression, evaluate" -> classic stack: push operands, and on an operator pop the two most recent operands and push the result back.

**Approach:** Keep a dict mapping each operator to a lambda taking `(x, y)`. Iterate tokens; push numbers as ints. On an operator, pop twice into `x` (top of stack, i.e. the more recently pushed operand) and `y` (the one below it), apply `valid_operators[token](x, y)`, and push the result. The lambdas are written as `y op x` so operand order comes out correct for non-commutative ops (`-`, `/`).

**Where I lost time:** This took the longest of the batch (~25 min), most likely on getting the operand order right for `-` and `/` — `stack.pop()` twice gives you the *second* operand first, so the lambda has to apply it as `y - x` / `y / x` rather than the naive `x - y`, which is easy to get backwards on the first pass.

**Complexity:** O(n) time, O(n) space (stack holds up to ~n/2 intermediate values in the worst case).

**Redo:** no
