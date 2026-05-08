class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            checkedNumber = nums[i]
            for j in range(len(nums)):
                if i != j:
                    if nums[i] == nums[j]:
                        return True
        return False