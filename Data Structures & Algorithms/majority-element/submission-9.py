import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        while True:
            candidate = random.choice(nums)
            if nums.count(candidate) > len(nums) // 2:
                return candidate