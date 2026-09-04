"""
0036. Valid Sudoku (Medium)
https://leetcode.com/problems/valid-sudoku/
Solved 2026-08-28 | <5 min | unaided
Time O(1) / Space O(1) - The board size is fixed (9x9)
Notes: notes.md
"""
from collections import defaultdict

def isValidSudoku(board: list[list[str]]) -> bool:
    col_dict = defaultdict(set)
    row_dict = defaultdict(set)
    for i in range(0, len(board), 3):
        for j in range(0, len(board[0]), 3):
            curr_box = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    curr = board[row][col]
                    if curr != ".":
                        if curr in row_dict[row] or curr in col_dict[col] or curr in curr_box:
                            return False
                        curr_box.add(curr)
                        row_dict[row].add(curr)
                        col_dict[col].add(curr)
    return True
