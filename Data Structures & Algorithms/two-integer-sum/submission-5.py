class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsCopy = []
        for i, num in enumerate(nums):
            numsCopy.append([num, i])
        numsCopy.sort()
        print(numsCopy)

        pointerOne = 0
        pointerTwo = len(nums) - 1

        for i in range(len(numsCopy)):
            if numsCopy[pointerOne][0] + numsCopy[pointerTwo][0] == target:
                return [min(numsCopy[pointerOne][1], numsCopy[pointerTwo][1]),
                        max(numsCopy[pointerOne][1], numsCopy[pointerTwo][1])]
                
            elif numsCopy[pointerOne][0] + numsCopy[pointerTwo][0] < target:
                pointerOne += 1

            else:
                pointerTwo -= 1 

        return []