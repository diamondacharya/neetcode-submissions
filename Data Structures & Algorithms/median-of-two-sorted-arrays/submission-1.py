class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter, longer = nums1, nums2 
        if len(nums2) < len(nums1): 
            shorter, longer = nums2, nums1 
        totalLen = len(shorter) + len(longer)
        half = totalLen // 2
        l, r = 0, len(shorter)
        while True: 
            i = l + (r - l) // 2      # i is the mid here
            j = half - i
            sLeft = shorter[i - 1] if i > 0 else float('-inf') 
            sRight = shorter[i] if i < len(shorter) else float('inf')
            lLeft = longer[j - 1] if j > 0 else float('-inf') 
            lRight = longer[j] if j < len(longer) else float('inf')
            if sLeft <= lRight and sRight >= lLeft:  # valid partition
                if totalLen % 2 != 0: 
                    return min(sRight, lRight)
                else: 
                    return (max(sLeft, lLeft) + min(sRight, lRight)) / 2
            elif sLeft > lRight: 
                r = i - 1
            else: 
                l = i + 1

        


