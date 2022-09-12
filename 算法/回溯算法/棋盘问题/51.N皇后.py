class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        self.used_col = set()
        self.used_diag = set()
        self.used_diag2 = set()

    def solveNQueens(self, n: int) -> List[List[str]]:

        def dfs(row):
            if row == n:
                self.ans.append(self.path[:])
                return

            for i in range(n):
                if i in self.used_col or i - row in self.used_diag or i + row in self.used_diag2:
                    continue

                self.used_col.add(i)
                self.used_diag.add(i - row)
                self.used_diag2.add(i + row)
                self.path.append('.' * i + 'Q' + '.' * (n - i - 1))
                dfs(row + 1)
                self.used_col.remove(i)
                self.used_diag.remove(i - row)
                self.used_diag2.remove(i + row)
                self.path.pop()

        dfs(0)
        return self.ans
