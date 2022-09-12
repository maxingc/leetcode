class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, total):
            if total>target:
                return
            if total == target:
                ans.append(path[:])
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(i+1, total+candidates[i])
                path.pop()

        ans = []
        path = []
        dfs(0, 0)
        return ans
