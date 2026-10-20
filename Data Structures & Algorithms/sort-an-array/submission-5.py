class Solution:
    def merge(self, nums: List[int], left: int, middle: int, right: int) -> None:
        leftArr, rightArr = nums[left:middle+1], nums[middle+1:right+1]
        i, j, k = left, 0, 0

        while j < len(leftArr) and k < len(rightArr):
            if leftArr[j] <= rightArr[k]:
                nums[i] = leftArr[j]
                j += 1
            else:
                nums[i] = rightArr[k]
                k += 1
            i += 1
        
        while j < len(leftArr):
            nums[i] = leftArr[j]
            j += 1
            i += 1

        while k < len(rightArr):
            nums[i] = rightArr[k]
            k += 1
            i += 1

    def mergeSort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        middle = (left + right) // 2
        self.mergeSort(nums, left, middle)
        self.mergeSort(nums, middle + 1, right)
        self.merge(nums, left, middle, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
