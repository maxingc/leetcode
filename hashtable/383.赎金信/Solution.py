class Solution:

    ##defaultdict
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hashmap = collections.defaultdict(int)
        for x in magazine:
            hashmap[x] += 1

        for x in ransomNote:
            n = hashmap.get(x)
            if n is None or n == 0:
                return False
            hashmap[x] -= 1

        return True

    ##Counter
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        x = c1 - c2
        # x只保留值大于0的符号，当c1里面的符号个数小于c2时，不会被保留
        # 所以x只保留下了，magazine不能表达的
        if (len(x) == 0):
            return True
        else:
            return False