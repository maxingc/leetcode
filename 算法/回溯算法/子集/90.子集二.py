class Solution:
    def __init__(self):
        self.ans = [[]]
        self.path = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(index):
            if index==len(nums):
                return
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                self.path.append(nums[i])
                self.ans.append(self.path[:])
                dfs(i+1)
                self.path.pop()

        nums = sorted(nums)
        dfs(0)
        return self.ans