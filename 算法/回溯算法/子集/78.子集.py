from typing import List


class Solution:
    def __init__(self):
        self.ans = [[]]
        self.path = []
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(index):
            if index==len(nums):
                return
            for i in range(index,len(nums)):
                self.path.append(nums[i])
                self.ans.append(self.path[:])
                dfs(i+1)
                self.path.pop()

        dfs(0)

        return self.ans


if __name__=='__main__':
    test = Solution()
    print(test.subsets([1,2,3]))