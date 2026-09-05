# 0036. Valid Sudoku

**Trigger:** "no repeated digit in any row/column/3x3 box" -> membership checks across three overlapping groupings -> a hash set per row, per column, and per box.

**Approach:** Walk the board one 3x3 box at a time. Inside each box, walk its 9 cells; for every filled cell check if the digit is already in that row's set, that column's set, or the current box's set — if so, fail immediately. Otherwise record the digit in all three sets and continue. If no collision is found anywhere, the board is valid.

**Where I lost time:** Nowhere much (<5 min) — the only fiddly part was getting the nested box/row/col index math right (`range(i, i+3)` / `range(j, j+3)`).

**Complexity:** Board is fixed at 9x9, so technically O(1) time / O(1) space (as noted in the file). In general n x n terms this pattern is O(n^2) time and O(n^2) space for the row/col/box sets.

**Redo:** no
