class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freqArr = list(freq.items())
        freqArr.sort(key=lambda x: x[1], reverse=True)

        returnArr = []

        for i in range(k):
            returnArr.append(freqArr[i][0])

        return returnArr