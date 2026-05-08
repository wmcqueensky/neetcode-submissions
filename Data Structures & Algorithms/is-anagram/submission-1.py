class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sortedS = sorted(s)
        sortedT = sorted(t)

        letterOccurences1 = {}
        letterOccurences2 = {}
        
        for letter in range(len(s)):
            letterOccurences1[sortedS[letter]] =  letterOccurences1.get(sortedS[letter], 0) + 1
            letterOccurences2[sortedT[letter]] =  letterOccurences2.get(sortedT[letter], 0) + 1

        if letterOccurences1 == letterOccurences2:
            return True
        
        return False
        
        
