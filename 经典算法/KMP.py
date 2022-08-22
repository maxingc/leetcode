class KMP:
    def get_next(self, s):
        next = [0] * (len(s)+1)
        i, j = 0, -1
        next[0] = -1
        while (i < len(s)):
            if j == -1 or s[i] == s[j]:
                i+=1
                j+=1
                next[i] = j
            else:
                j = next[j]
        return next

    def kmp(self, target, s):
        i=j=0
        next = self.get_next(target)

        while i<len(target) and j<len(s):
            if j==-1 or target[i]==s[j]:
                i+=1
                j+=1
            else:
                j=next[j]

