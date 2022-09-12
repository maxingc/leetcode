class Solution:
    ##最大堆
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        ans = []
        q = [(-nums[i], i) for i in range(k - 1)]
        heapq.heapify(q)
        for i in range(k - 1, len(nums)):
            while q and q[0][1] <= i - k:
                heapq.heappop(q)
            heapq.heappush(q, (-nums[i], i))
            ans.append(-q[0][0])
        return ans

    ##优先队列&堆
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        ans = []
        for i in range(k - 1):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        for i in range(k - 1, len(nums)):
            while q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans



