class Solution:
    # piles = [1, 4, 3, 2]
    # h = 9
    # -------------
    # l = 1, r = 4, k = 2, hoursTaken = 6
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # we'll do binary search to find the min k
        res = 0
        while l <= r: 
            k = l + (r - l) // 2 # k will be our mid
            hoursTaken = 0
            for num in piles: 
                hoursTaken += math.ceil(num/k)
            if hoursTaken <= h: # means you can take more hours to eat (can reduce k)
                res = k
                r = k - 1
            else: 
                l = k + 1
        return res

            