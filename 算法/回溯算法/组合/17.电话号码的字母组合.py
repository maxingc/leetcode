class Solution:
    def __init__(self):
        self.ans = []
        self.digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, option):
            if index == len(digits):
                self.ans += [option]
                return

            letters = self.digit_map[digits[index]]
            for letter in letters:
                dfs(index + 1, option + letter)

        if len(digits) == 0:
            return []
        dfs(0, '')
        return self.ans