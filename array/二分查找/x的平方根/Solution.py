class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            middle = (left + right) // 2
            if middle * middle <= x:
                left = middle + 1
            else:
                right = middle - 1

        return (left - 1)

    ## newton
    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0
        x0 = x
        while True:
            xi = 0.5 * (x0 + x / x0)
            if x0 - xi < 1e-7:
                return int(xi)
            x0 = xi
