class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        stack = []
        counter = 0
        counter_rep = 0
        max_seq = 0
        for letter in s:
            print("pass1")
            if not stack or letter in stack:
                print("pass")
                stack.append(letter)
                counter += 1
                max_seq = max(max_seq,counter)
            else:
                if counter_rep < k:
                    stack.append(stack[0])
                    counter += 1
                    counter_rep += 1
                    max_seq = max(max_seq,counter)
                else:
                    stack = [letter]
                    counter = 1
                    counter_rep = 0
            print(stack)
        print(max_seq)
        return max_seq


        