class Solution:
    def __init__(self):
        self.path = ['JFK']
        self.used_set = set()

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(deep, start):
            if deep == len(tickets):
                return True

            if start in dic:
                for x in dic[start]:
                    if x[1] in self.used_set:
                        continue
                    self.path.append(x[0])
                    self.used_set.add(x[1])
                    if dfs(deep + 1, x[0]):
                        return True
                    self.used_set.remove(x[1])
                    self.path.pop()

        dic = {}
        for i, r in enumerate(tickets):
            if r[0] not in dic:
                dic[r[0]] = []
            dic[r[0]].append((r[1], i))

        for k in dic:
            dic[k].sort()

        dfs(0, 'JFK')
        return self.path

if __name__=="__main__":
    test = Solution()
    print(test.findItinerary([["EZE","TIA"],["EZE","AXA"],["AUA","EZE"],["EZE","JFK"],["JFK","ANU"],["JFK","ANU"],["AXA","TIA"],["JFK","AUA"],["TIA","JFK"],["ANU","EZE"],["ANU","EZE"],["TIA","AUA"]]))