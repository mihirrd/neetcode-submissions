class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(num):
            multiplier = 1
            res = 0
            for n in num[::-1]:
                digit = ord(n) - ord("0")
                res += digit*multiplier
                multiplier *= 10
            return res
        
        multiplication = str_to_int(num1) * str_to_int(num2)
        return str(multiplication)