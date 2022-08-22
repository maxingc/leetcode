class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_next(s):
            next = [0] * (len(s) + 1)
            i, j = 0, -1
            next[0] = -1
            while (i < len(s)):
                if j == -1 or s[i] == s[j]:
                    i += 1
                    j += 1
                    next[i] = j
                else:
                    j = next[j]

            return next

        next = get_next(needle)
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]

        if j == len(needle):
            return i - len(needle)
        else:
            return -1