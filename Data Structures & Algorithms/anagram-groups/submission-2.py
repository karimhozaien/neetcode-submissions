class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big = {}
        small = {}
        for word in strs:
            array = [0]*26
            for letter in word:
                array[ord(letter) - ord('a')] += 1
            if str(array) in big.keys():
                big[str(array)].append(word)
            else:
                big[str(array)] = [word]
        return list(big.values())

        