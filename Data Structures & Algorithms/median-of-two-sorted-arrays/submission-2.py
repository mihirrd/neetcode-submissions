class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #nusm1 should be the shorter one
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        l,r = 0,len(nums1)
        total = len(nums1) + len(nums2)
        is_even = total % 2 == 0
        half = total//2
        while l <= r:
            i = (l + r)//2 
            # let's say we take i elements from nums1
            # from num2 we will take half - i elements
            j = half - i # index tracking num2
            aleft = nums1[i-1] if i > 0 else float("-inf")
            aright = nums1[i] if i < len(nums1) else float("inf")
            bleft = nums2[j-1] if j > 0 else float("-inf")
            bright = nums2[j] if j < len(nums2) else float("inf")

            # invariant: aleft and bleft have to be lesser than aright and bright
            # aleft > bright, i have to move left
            # aright < bleft, i have to move right
            if aleft <= bright and bleft <= aright:
                if is_even:
                    return (max(aleft,bleft) + min(aright, bright))/2
                else:
                    return min(aright, bright)
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1
