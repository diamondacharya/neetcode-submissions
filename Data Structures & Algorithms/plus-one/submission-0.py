class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1): 
            summ = digits[i] + carry
            digits[i] = summ % 10 
            carry = summ // 10
        return digits if not carry else [1] + digits