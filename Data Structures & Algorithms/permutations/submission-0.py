class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _perm(i):
            if i == len(nums):
                res.append(nums[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j] = nums[j],nums[i]
                _perm(i+1)
                nums[i],nums[j] = nums[j],nums[i]
        
        _perm(0)
        return res