class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))

    def rob1(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums)+1)
        def _rob(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            take = nums[i] + _rob(i+2)
            skip = _rob(i+1)
            dp[i] = max(take, skip)
            return dp[i]
        
        return _rob(0)
        
