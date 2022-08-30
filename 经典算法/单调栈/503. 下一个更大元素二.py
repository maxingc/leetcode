class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        queue = []
        l = len(nums)
        ans = [-1] * l
        nums = nums + nums
        for i in range(len(nums)):
            while queue and nums[queue[-1]]<nums[i]:
                ans[queue.pop()] = nums[i]
            if i<l:
                queue.append(i)
        return ans
