class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ans = float('inf')
        j = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum>=target:
                ans = min(ans, i-j+1)
                sum -= nums[j]
                j+=1

        return ans if ans!=float('inf') else 0