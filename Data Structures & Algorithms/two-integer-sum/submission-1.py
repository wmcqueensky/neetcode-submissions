class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexOne = 0
        indexTwo = 0
        numberOne = 0
        numberTwo = 0

        for i in range(len(nums)):
            numberOne = nums[i]
            for j in range(len(nums)):
                if i == j:
                    continue
                numberTwo = nums[j]
                
                if numberOne + numberTwo == target:
                    return [i, j]
        return []