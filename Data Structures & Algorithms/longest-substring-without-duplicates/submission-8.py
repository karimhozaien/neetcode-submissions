class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i in range(len(s)):
            l,r = i,i
            sub = ""
            length = 0
            while r < len(s) and s[r] not in sub:
                sub+=s[r]
                length = len(sub)
                if length > longest:
                    longest = length
                r+=1
        return longest
        