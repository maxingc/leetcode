class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        self.used_set = set()
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(self.path)==len(nums):
                self.ans.append(self.path[:])
                return
            for i in range(len(nums)):
                if nums[i] in self.used_set:
                    continue
                self.used_set.add(nums[i])
                self.path.append(nums[i])
                dfs()
                self.path.pop()
                self.used_set.remove(nums[i])
        dfs()
        return self.ans