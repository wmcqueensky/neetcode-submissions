class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]

        if len(strs) == 1:
            return [[strs[0]]]

        mappings = {}
        for i in range(len(strs)):
            sortedStringList = sorted(strs[i])
            sortedString = "".join(sortedStringList)
            if sortedString not in mappings:
                mappings[sortedString] = [strs[i]]
            else:
                mappings[sortedString].append(strs[i])
        
        returnTable = []
        for key in mappings:
            returnTable.append(mappings[key])
        return returnTable
            