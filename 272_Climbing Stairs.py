class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n <=1:
            return 1

        if n==2:
            return 2
        
        a,b,c = 1,1,2
        for i in range(3, n+1):
            a,b,c = b, c, a+b+c
        return c
