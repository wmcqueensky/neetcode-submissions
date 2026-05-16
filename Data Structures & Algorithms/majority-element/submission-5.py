class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        numsCopy = sorted(nums)
        return numsCopy[len(nums) // 2]