from typing import List


class Solution:
    # O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

            return []

    # O(n) Hash Table
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target-num], i]
            hash_table[num] = i

        return []



