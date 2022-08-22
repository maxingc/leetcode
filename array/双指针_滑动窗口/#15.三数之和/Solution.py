class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                while (nums[first] + nums[second] + nums[third] < 0 or (
                        second - 1 > first and nums[second] == nums[second - 1])) and second < third:
                    second += 1
                while (nums[first] + nums[second] + nums[third] > 0 or (
                        third + 1 < len(nums) - 1 and nums[third] == nums[third + 1])) and second < third:
                    third -= 1
                if second < third and nums[first] + nums[second] + nums[third] == 0:
                    ans += [[nums[first], nums[second], nums[third]]]
                    second += 1
                    third -= 1

        return ans