class Solution:
    def reverse(self, x: int) -> int:
        ekak = 0     
        num = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            ekak = x % 10
            num += ekak
            num *= 10
            x = x//10
        res = (sign * num)//10
        return res if res <= 2**31-1 and res >= -2**31 else 0