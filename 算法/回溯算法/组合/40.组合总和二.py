class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, total):
            if total>target:
                return
            if total == target:
                ans.append(path[:])
                return

            for i in range(index, len(candidates)):
                if i>index and i>0 and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, total+candidates[i])
                path.pop()

        ans = []
        path = []
        candidates = sorted(candidates)
        dfs(0, 0)
        return ans