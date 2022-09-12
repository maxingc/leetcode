#回文串判断
##动态规划
f = [[True] * n for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

##记忆化搜索
@cache
def isPalindrome(i: int, j: int) -> int:
    if i >= j:
        return 1
    return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

##倒序
s == s[::-1]


