"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check(board, row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            if board[row][col] == 1:
                return 1
            else:
                return 0

        m = len(board)
        n = len(board[0])
        save = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                count = check(board, row - 1, col - 1) + check(board, row, col - 1) + check(board, row + 1, col - 1) + check(board, row - 1,col) + \
                        check(board, row + 1, col) + check(board, row - 1, col + 1) + check(board, row, col + 1) + check(board,row + 1,col + 1)
                if board[row][col] == 0:
                    if count == 3:
                        save[row][col] = 1
                    else:
                        save[row][col] = 0
                else:
                    if count < 2 or count > 3:
                        save[row][col] = 0
                    else:
                        save[row][col] = 1
        for i in range(m):
            board[i] = save[i]