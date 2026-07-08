class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1]*len(nums)
        parent = [-1]*len(nums)
        max_idx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
                    parent[i] = j
            
            if dp[max_idx] < dp[i]:
                max_idx = i
        
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = parent[max_idx]

        return res

