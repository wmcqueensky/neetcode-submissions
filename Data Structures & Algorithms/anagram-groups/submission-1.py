class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]

        if len(strs) == 1:
            return [[strs[0]]]

        strsCopy = []

        for string in strs:
            strsCopy.append(sorted(string))
        
        returnTable = []
        insertSubTable = []
        presenceChecker = set()
        checkedAnagram = ""

        for i in range(len(strsCopy)):
            checkedAnagram = strsCopy[i]
            if "".join(checkedAnagram) in presenceChecker:
                continue
            
            presenceChecker.add("".join(strsCopy[i]))

            for j in range(len(strsCopy)):
                if strsCopy[j] == checkedAnagram:
                    insertSubTable.append(strs[j])

            if len(insertSubTable) != 0:
                returnTable.append(insertSubTable)
                insertSubTable = []
       
        return returnTable