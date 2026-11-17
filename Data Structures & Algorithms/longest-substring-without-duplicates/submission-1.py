class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        max_counter = 0
        stack = []
        for letter in s:
            if letter in stack:
                stack = []
                max_counter = max(counter,max_counter)
                stack.append(letter)
                counter = 1
            else:
                stack.append(letter)
                counter += 1
            print(stack)
            print(counter)
        return max_counter


        