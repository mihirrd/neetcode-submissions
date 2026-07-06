class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))

    def rob1(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+2)
        for i in range(len(nums)-1,-1,-1):            
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        return dp[0]
        
