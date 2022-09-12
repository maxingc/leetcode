class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        self.used_pos_set = set()
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(self.path)==len(nums):
                self.ans.append(self.path[:])
                return
            used_num_set =set()
            for i in range(len(nums)):
                if i in self.used_pos_set or nums[i] in used_num_set:
                    continue
                self.used_pos_set.add(i)
                used_num_set.add(nums[i])
                self.path.append(nums[i])
                dfs()
                self.path.pop()
                self.used_pos_set.remove(i)
        dfs()
        return self.ans