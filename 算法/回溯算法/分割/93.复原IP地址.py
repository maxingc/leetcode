class Solution:
    def __init__(self):
        self.ans = []
        self.path = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(index):
            if len(self.path) == 4:
                if index == len(s):
                    self.ans.append(".".join(self.path[:]))
                return

            for i in range(index, min(index + 3, len(s))):
                if s[index] == '0' and i > index:
                    continue
                num = int(s[index:i + 1])
                if num <= 255:
                    self.path.append(s[index:i + 1])
                    dfs(i + 1)
                    self.path.pop()

        dfs(0)
        return self.ans

