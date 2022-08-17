from typing import List


class Solution:
    ##快慢指针
    def removeElement(self, nums: List[int], val: int) -> int:
        slow_index, fast_index = 0, 0
        l = len(nums)
        while fast_index < l:
            if nums[fast_index] != val:
                nums[slow_index] = nums[fast_index]
                slow_index += 1
            fast_index += 1

        return slow_index

    ##双向指针
    def removeElement2(self, nums: List[int], val: int) -> int:
        l = len(nums)
        left_index, right_index = 0, l - 1

        while left_index <= right_index:
            while (left_index < l) and (nums[left_index] != val):
                left_index += 1
            while (right_index >= 0) and (nums[right_index] == val):
                right_index -= 1
            if (left_index < l) and (right_index >= 0) and (left_index <= right_index):
                nums[left_index], nums[right_index] = nums[right_index], nums[left_index]

        return left_index


