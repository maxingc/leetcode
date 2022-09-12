class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(row, col):
            if row == 9:
                return True
            if board[row][col] != '.':
                flag = dfs(row + 1, 0) if col == 8 else dfs(row, col + 1)
                if flag:
                    return True
            else:
                for i in range(9):
                    if row_flag[row][i] or col_flag[col][i] or zone_flag[row // 3 * 3 + col // 3][i]:
                        continue
                    row_flag[row][i] = True
                    col_flag[col][i] = True
                    zone_flag[row // 3 * 3 + col // 3][i] = True
                    board[row][col] = str(i + 1)
                    flag = dfs(row + 1, 0) if col == 8 else dfs(row, col + 1)
                    if flag:
                        return True
                    row_flag[row][i] = False
                    col_flag[col][i] = False
                    zone_flag[row // 3 * 3 + col // 3][i] = False
                    board[row][col] = '.'

        row_flag = [[False for i in range(9)] for j in range(9)]
        col_flag = [[False for i in range(9)] for j in range(9)]
        zone_flag = [[False for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_flag[i][int(board[i][j]) - 1] = True
                    col_flag[j][int(board[i][j]) - 1] = True
                    zone_flag[i // 3 * 3 + j // 3][int(board[i][j]) - 1] = True

        dfs(0, 0)
        return board



