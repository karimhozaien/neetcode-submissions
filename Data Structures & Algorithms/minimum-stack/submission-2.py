class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif val <= self.minstack[len(self.minstack)-1]:
            self.minstack.append(val)
        


    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack[-1] == self.minstack[-1]:
                self.stack.pop()
                self.minstack.pop()
            else:
                self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
                

            

