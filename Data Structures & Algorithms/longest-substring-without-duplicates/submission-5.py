class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        max_counter = 0
        stack = []
        for letter in s:
            if letter in stack:
                while letter in stack:
                    stack.reverse()
                    stack.pop()
                    stack.reverse()
                max_counter = max(counter,max_counter)
                stack.append(letter)
                counter = len(stack)
            else:
                stack.append(letter)
                counter += 1
                max_counter = max(counter,max_counter)
            print(stack)
            print(counter)
        return max_counter


        