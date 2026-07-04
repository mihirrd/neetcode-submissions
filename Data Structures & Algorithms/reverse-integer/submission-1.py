class Solution:
    def reverse(self, x: int) -> int:
        digit = 0     
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            digit = x % 10
            x = x // 10
            if res * 10 > 2**31 - 1:
                return 0
            res = (res * 10) + digit
        return res * sign