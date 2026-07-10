class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        cache = {}
        def max_coins(nums):
            if len(nums) == 1:
                return nums[0]
            
            if tuple(nums) in cache:
                return cache[tuple(nums)]
            res = float("-inf")            
            for i in range(len(nums)):
                curr = 0
                if i == 0:
                    curr += (nums[0] * nums[1] + max_coins(nums[1:]))
                elif i == len(nums)-1:
                    curr += (nums[-2] * nums[-1] + max_coins(nums[:-1]))
                else:
                    curr += (nums[i-1] * nums[i] * nums[i+1] + max_coins(nums[:i] + nums[i+1:]))
                res = max(res, curr)
            
            cache[tuple(nums)] = res
            return res
        
        return max_coins(nums)