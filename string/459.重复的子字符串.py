class Solution:
    ##kmp
    def repeatedSubstringPattern(self, s: str) -> bool:
        def get_next(s):
            next = [0] * (len(s)+1)
            i , j = 0, -1
            next[0] = -1
            while i<len(s):
                if j==-1 or s[i]==s[j]:
                    i+=1
                    j+=1
                    next[i]=j
                else:
                    j=next[j]
            return next

        def kmp(query, pattern):
            next = get_next(pattern)
            i=j=0
            while i<len(query) and j<len(pattern):
                if j==-1 or query[i]==pattern[j]:
                    i+=1
                    j+=1
                else:
                    j = next[j]
            if j==len(pattern):
                return True
            else:
                return False

        return kmp((s+s)[1:-1], s)
    ##优化kmp
    def repeatedSubstringPattern2(self, s: str) -> bool:
        def get_next(s):
            next = [0] * (len(s)+1)
            i , j = 0, -1
            next[0] = -1
            while i<len(s):
                if j==-1 or s[i]==s[j]:
                    i+=1
                    j+=1
                    next[i]=j
                else:
                    j=next[j]
            return next

        next = get_next(s)
        return len(s) % (len(s) - next[len(s)])==0 and next[len(s)]!=0
