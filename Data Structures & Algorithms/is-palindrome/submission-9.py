class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ss = "".join(s)
        stack =[]
        for i in range(len(ss)):
            if ss[i].isalnum():
                stack.append(ss[i])
        l = 0
        r = len(stack) -1
        while l < r:
            print(stack[l], stack[r])
            if stack[l] != stack[r]:
                return False
            r-=1
            l+=1
        return True