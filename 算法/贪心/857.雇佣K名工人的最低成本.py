from heapq import heappush, heappop, heappushpop
from math import inf


class Solution:

    ## priority queue
    ####heappushpop
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(wage, quality), key= lambda x: x[0]/x[1])
        h = []
        sum_q = 0
        for w, q in pairs[:k]:
            sum_q += q
            heappush(h, -q)
        ans = sum_q * w/q
        for w, q in pairs[k:]:
            sum_q += q
            sum_q += heappushpop(h, -q)
            ans = min(ans, sum_q * w/q)
        return ans

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(wage, quality), key=lambda x: x[0] / x[1])
        h = []
        sum_q = 0
        ans = inf
        for w, q in pairs[:k - 1]:
            sum_q += q
            heappush(h, -q)
        for w, q in pairs[k - 1:]:
            sum_q += q
            heappush(h, -q)
            ans = min(ans, sum_q * w / q)
            sum_q += heappop(h)

        return ans


            ##my answer
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        l = len(quality)
        zip_list = []
        for i in range(l):
            zip_list.append((float(wage[i] / quality[i]), i))
        zip_list = sorted(zip_list)

        sub_quality = []
        for i in range(k):
            sub_quality.append(float(quality[zip_list[i][1]]))
        ans = sum([x * zip_list[k - 1][0] for x in sub_quality])

        for i in range(k, l):
            sub_quality.append(float(quality[zip_list[i][1]]))
            sub_quality = sorted(sub_quality)
            ans = min(ans, sum(x * zip_list[i][0] for x in sub_quality[:k]))

        return ans
