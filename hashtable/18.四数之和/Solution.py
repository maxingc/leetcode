class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        dic = collections.defaultdict(int)
        for x in nums:
            dic[x] += 1

        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - nums[i] - nums[j] - nums[k]
                    if val in dic:
                        cnt = dic[val] - ((nums[i] == val) + (nums[j] == val) + (nums[k] == val))
                        if cnt > 0:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))

        return list(ans)

