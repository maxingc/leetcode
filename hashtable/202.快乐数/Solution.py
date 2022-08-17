class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_happy_num(x):
            sum_ = 0
            while x>0:
                sum_ += (x % 10) ** 2
                x = x // 10
            return sum_

        record = set()
        record.add(n)
        while True:
            n = calculate_happy_num(n)
            if n==1:
                return True
            if n in record:
                return False
            record.add(n)
        return