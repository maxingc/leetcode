class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0] * n for _ in range(n)]
        loops = (n + 1) // 2
        start_x, start_y = 0, 0
        num = 1

        for loop in range(loops):
            i, j = loop, loop
            for j in range(loop, n - loop):
                matrix[i][j] = num
                num += 1
            for i in range(loop + 1, n - loop):
                matrix[i][j] = num
                num += 1
            for j in range(n - loop - 2, loop - 1, -1):
                matrix[i][j] = num
                num += 1
            for i in range(n - loop - 2, loop, -1):
                matrix[i][j] = num
                num += 1

        return matrix
