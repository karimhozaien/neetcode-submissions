class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        my_list = list(s)
        left = 0
        right = len(my_list)-1
        while left <= right:
            while not my_list[left].isalpha():
                left+=1
            while not my_list[right].isalpha():
                right-=1
            if my_list[right] != my_list[left]:
                return False
            left+=1
            right-=1
        return True
            
        

        