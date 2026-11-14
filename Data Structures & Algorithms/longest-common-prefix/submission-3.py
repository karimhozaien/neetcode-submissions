class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack = []
        stacks = ""
        for i in range(len(strs)):
            if i == 0:
                for j in range(len(strs[0])):
                    stack.append(strs[0][j])
                    stacks = ''.join(stack)
                    empty = ""
                    print(stack)
                    if not stack:
                        return empty
            elif stack:
                if stacks == strs[i]:
                    continue
                else:
                    while stacks not in strs[i] and len(stack) > 0:
                        print('yes')
                        stack.pop()
                        print(stack)
                        stacks = ''.join(stack)
                        print(stacks)
        return stacks
        