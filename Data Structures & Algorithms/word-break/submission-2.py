# s = "abcd" -->  len 4
# wordDict = ['a', 'abc', 'b', 'cd']
# boolarr = [false,true,true,false,true]  --> len 5
# i = 3 
# i = 2
#     cd 
#         boolarr[2] = boolarr[4]
# i = 1  
#     b
#         boolarr[1] = boolarr[2]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        boolarr = [False] * (len(s) + 1)
        boolarr[-1] = True  # base case
        for i in range(len(s) - 1, -1, -1): 
            for word in wordDict: 
                if i + len(word) <= len(s) and s[i:i+len(word)] == word: 
                    boolarr[i] = boolarr[i + len(word)]
                if boolarr[i]: 
                    break
        return boolarr[0]
            


