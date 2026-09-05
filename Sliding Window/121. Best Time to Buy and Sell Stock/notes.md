# 0121. Best Time to Buy and Sell Stock

**Trigger:** "max profit from a single buy/sell" -> track the running minimum price seen so far (buy point) while scanning once, comparing against the best profit found.

**Approach:** `left_ptr` tracks the index of the lowest price seen so far, `right_ptr` scans forward. If the price at `left_ptr` is `>=` the price at `right_ptr`, a new (lower-or-equal) low has been found, so snap `left_ptr` to `right_ptr`. Otherwise advance `right_ptr` and compute the profit against the current low, updating `max_profit`. Guards against an empty input and clamps a negative result to 0.

**Where I lost time:** Moderate (~10 min) — the two-pointer "reset left to right on a new low" mechanic is a slightly indirect way to track a running minimum, and the order of "reset, then advance right, then compute profit" likely took some care to get the indices to line up correctly.

**Complexity:** O(n) time, O(1) space.

**Redo:** no
