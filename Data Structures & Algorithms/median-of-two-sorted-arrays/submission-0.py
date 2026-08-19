class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter, longer = nums1, nums2
        if len(longer) < len(shorter): 
            shorter, longer = longer, shorter
        total = len(shorter) + len(longer)
        half = total // 2
        l, r = 0, len(shorter) - 1
        while True: 
            mid = l + (r - l) // 2
            longerMid = half - mid - 2 # it's an index. come up with offset with concrete ex.
            # values at the paritition points
            shorterLeft = shorter[mid] if mid >= 0 else float('-inf')
            shorterRight = shorter[mid + 1] if (mid + 1) < len(shorter) else float('inf')
            longerLeft = longer[longerMid] if longerMid >= 0 else float('-inf')
            longerRight = longer[longerMid + 1] if (longerMid + 1) < len(longer) else float('inf')
            # If, valid parition found, we return; else, we move pointer to find valid partition 
            if shorterLeft <= longerRight and longerLeft <= shorterRight:  
                if total % 2: # odd legth
                    return min(shorterRight, longerRight)
                else: 
                    return (max(shorterLeft, longerLeft) + min(shorterRight, longerRight)) / 2
            elif shorterLeft > longerRight: 
                r = mid - 1
            else: 
                l = mid + 1


                