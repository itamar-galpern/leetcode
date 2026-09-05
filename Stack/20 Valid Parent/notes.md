# 0020. Valid Parentheses

**Trigger:** "brackets must close in the right order" -> stack: push openers, and on a closer check it matches the most recently opened bracket.

**Approach:** Iterate characters; if it's an opening bracket, push it. If it's a closer, pop the stack (fail if empty) and check the popped opener matches what this closer expects via a `closer -> opener` lookup dict. At the end, the string is valid only if the stack is empty (no unclosed openers left).

**Where I lost time:** Nowhere, immediate answer (<5 min).

**Complexity:** O(n) time, O(n) space (stack can hold up to n openers in the worst case).

**Redo:** no
