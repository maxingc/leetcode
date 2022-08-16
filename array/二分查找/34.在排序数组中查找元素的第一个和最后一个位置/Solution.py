from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        left_bound, right_bound = -1, -1

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        if (left >= len(nums)) or (nums[left] != target):
            return [-1, -1]
        else:
            left_bound = left

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1

        right_bound = right

        return [left_bound, right_bound]

