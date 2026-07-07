class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1]*len(nums)
        parent = [-1]*len(nums)
        max_idx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i 
        
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = parent[max_idx]

        return res[::-1]