# Problem Statement: https://leetcode.com/problems/valid-sudoku/
# The function checks if a given 9x9 Sudoku board is valid.
# A Sudoku board is valid if:
#   - Each row contains the digits 1-9 without repetition.
#   - Each column contains the digits 1-9 without repetition.
#   - Each of the 9 sub-boxes (3x3 grids) contains the digits 1-9 without repetition.
# Note:
#   - The board may contain empty cells represented by '.'.
# Input:
#   - board: A 9x9 2D list representing the Sudoku board.
# Output:
#   - A boolean value indicating whether the Sudoku board is valid.

# Time Complexity: O(9^2) - We iterate through all 81 cells in the board.
# Space Complexity: O(9) - We use hash maps to store the digits for rows, columns, and sub-boxes.

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_map={}
        for row in board:
            hash_map={}
            for value in row:
                if value != "." and value in hash_map :
                    return False
                hash_map[value]=1
        hash_map={}
        for col in zip(*board):
            hash_map={}
            for value in col:
                if value != "." and value in hash_map:
                    return False
                hash_map[value]=1
        hash_map=defaultdict(set)
        for i in range(9):
            for j in range(9):
                t = (i//3, j//3)
                value = board[i][j]
                if value != "." and value in hash_map[t]:
                    return False
                hash_map[t].add(value)
        print(hash_map)
        return True

if __name__ == "__main__":
    solution = Solution()

    # Example 1: Valid Sudoku
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print("Input:")
    for row in board:
        print(row)
    print("Output:", solution.isValidSudoku(board))  # Expected: True

    # Example 2: Invalid Sudoku (row conflict)
    board[0][1] = "5"  # Duplicate "5" in the first row
    print("\nInput:")
    for row in board:
        print(row)
    print("Output:", solution.isValidSudoku(board))  # Expected: False