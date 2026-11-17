class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            while j != '#':
                j+=1
            length = int(str[i:j])
            res.append(str[j +1: j+1 + length])
        return res


