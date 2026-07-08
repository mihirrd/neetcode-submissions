class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr = nums[0]
        for i in range(1,len(nums)):
            curr = max(curr + nums[i], nums[i])
            max_sum = max(curr, max_sum)
        return max_sum
