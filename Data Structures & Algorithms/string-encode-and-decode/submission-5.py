class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for string in  strs:
            encodedString += str(len(string)) + "#" + string
        return encodedString

    def decode(self, s: str) -> List[str]:
        i = 0
        decodedString = []
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            string = s[j + 1:j + 1 + length]
            decodedString.append(string)

            i = j + 1 + length
        
        return decodedString
