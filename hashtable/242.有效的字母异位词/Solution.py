class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        record = [0] * 26

        for x in s:
            record[ord(x) - ord('a')] += 1
        for x in t:
            record[ord(x) - ord('a')] -= 1

        for x in record:
            if x!=0:
                return False

        return True