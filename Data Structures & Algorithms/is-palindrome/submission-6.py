class Solution:
    def isPalindrome(self, s: str) -> bool:
        tab = []
        s = s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                tab.append(s[i])
        string = ''.join(tab)
        string_rev = ''.join(tab[::-1])
        if string == string_rev:
            return True
        return False


        