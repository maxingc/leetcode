class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, pre):
            if index==len(nums):
                return
            used_set = set()
            for i in range(index,len(nums)):
                if nums[i] in used_set:
                    continue
                used_set.add(nums[i])
                if nums[i]>=pre:
                    self.path.append(nums[i])
                    if len(self.path)>=2:
                        self.ans.append(self.path[:])
                    dfs(i+1, nums[i])
                    self.path.pop()
        dfs(0,float('-inf'))
        return self.ans