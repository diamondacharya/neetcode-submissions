#         3   4
#         5   6
#     ---------------
# .   .   2    4 
# .   .   .    . 
# .   .   .    . 

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in (num1, num2): 
            return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)): 
            for j in range(len(num2)): 
                toAdd = int(num1[i]) * int(num2[j])
                res[i + j] += toAdd
                res[i + j + 1] += (res[i + j] // 10)
                res[i + j] = res[i + j] % 10
        res = res[::-1]
        res = [str(digit) for digit in res]
        return "".join(res).lstrip('0') # strip leading zeros 
        