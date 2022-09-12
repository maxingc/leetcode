from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start_index, total):
            if total > n:
                return
            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                return

            for i in range(start_index, 9 - (k - len(path)) + 2):
                path.append(i)
                dfs(i + 1, total + i)
                path.pop()

        ans = []
        path = []
        dfs(1, 0)
        return ans


if __name__ =='__main__':
    ans = Solution()
    print(ans.combinationSum3(3,9))