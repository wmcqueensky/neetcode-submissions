class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        sortedStr = sorted(strs)
        for i in range(min(len(sortedStr[0]), len(sortedStr[-1]))):
            if sortedStr[0][i] != sortedStr[-1][i]:
                return sortedStr[0][:i]
        return sortedStr[0]