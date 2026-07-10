class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(n1, n2):
            if len(n1) == 0:
                return n2
            elif len(n2) == 0:
                return n1
            merged = []
            i,j = 0,0
            while i < len(n1) and j < len(n2):
                if n1[i] <= n2[j]:
                    merged.append(n1[i])
                    i += 1
                else:
                    merged.append(n2[j])
                    j += 1
            
            if i < len(n1):
                return merged + n1[i:]
            
            if j < len(n2):
                return merged + n2[j:]

        def _sort(nums):
            if len(nums) <= 1:
                return nums
            m = len(nums)//2
            left = _sort(nums[:m])
            right = _sort(nums[m:])
            return merge(left, right)
        
        return _sort(nums)

