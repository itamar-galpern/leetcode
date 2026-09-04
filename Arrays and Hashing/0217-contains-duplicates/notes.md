# 217. Contains duplicates

**Trigger:** "any value appears at least twice" / "element is distinct" -> Set membership
Anything asking "Have I seen this before?" is likely a set or a dict. 

**Aproach:** walk the array once, for each number ask "Have I seen it before?"
return True if yes, else add the number to the seen set and continue. If loop finishes, return False.

**Where I lost time:** Nowhere, immediate answer.

**Complexity:** O(n) space and time

**Redo:** no
