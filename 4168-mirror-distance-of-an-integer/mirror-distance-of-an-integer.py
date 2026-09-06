class Solution:
    def mirrorDistance(self, n: int) -> int:
        a = n
        b = 0
        last_zero = True
        while n > 0 :
            while last_zero:
                if n % 10 == 0:
                    n = n // 10
                else:
                    last_zero = False
            b = 10*b + n % 10
            n = n // 10
        return abs(a-b)
        