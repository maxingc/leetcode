from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:

        def dfs(index):
            if index >= len(s):
                self.ans.append(self.path[:])
                return

            for i in range(index, len(s)):
                sub_s = s[index:i + 1]
                if sub_s == sub_s[::-1]:
                    self.path.append(sub_s)
                    dfs(i + 1)
                    self.path.pop()

        dfs(0)
        return self.ans


