class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, num in enumerate(nums):
            numsDict[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in numsDict and numsDict[diff] != i:
                return [i, numsDict[diff]]
        return []