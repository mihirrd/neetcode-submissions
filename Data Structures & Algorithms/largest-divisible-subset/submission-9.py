class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return []
            if i in cache:
                return cache[i]
            res = [nums[i]]
            temp = []
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = [nums[j]] + dfs(j)
                if len(temp) > len(res):
                    res = temp
            
            cache[i] = res
            return res
        
        res = []
        for i in range(len(nums)):
            temp = dfs(i)
            if len(temp) > len(res):
                res = temp 
        
        return res