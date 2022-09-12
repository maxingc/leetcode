from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(start_index):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start_index, n - (k - len(path)) + 2):
                path.append(i)
                dfs(i + 1)
                path.pop()

        res = []
        path = []
        dfs(1)
        return res

