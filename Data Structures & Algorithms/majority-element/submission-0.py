class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dic = {}
        for num in range(len(nums)):
            dic[nums[num]] = dic.get(nums[num], 0) + 1

        biggest = list(dic.keys())[0]
        for i in dic.keys():
            if dic[biggest] < dic[i]:
                biggest = i
        return biggest