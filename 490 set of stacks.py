class SetOfStacks:
    """
    @param: capacity: An inetger, capacity of sub stack
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.stack=[]
        self.capacity = capacity

    """
    @param: v: An integer
    @return: nothing
    """
    def push(self, v):
        # write your code here
        if len(self.stack) ==0:
            self.stack.append([])
        if len(self.stack[-1]) == self.capacity:
            self.stack.append([])
        self.stack[-1].append(v)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        v=self.stack[-1].pop()
        if len(self.stack[-1]) is 0:
            self.stack.pop()
        return v
