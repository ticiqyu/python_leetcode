class Solution:
    def mirrorDistance(self, n: int) -> int:
        a = n
        while n % 10 == 0 and n > 0 :
            n = n//10
        b = 0
        while n > 0:
            b = 10*b + n % 10
            n = n // 10
        return abs(a-b)
        