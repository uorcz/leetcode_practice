class Solution:
    def reverse(self, x: int) -> int:
        if abs(x)>2147483647:
            return 0
        if int(str(abs(x))[::-1]) > 2147483647:
            return 0
        if x>0:
            return int(str(x)[::-1])
        else:
            return int(str(-1*x)[::-1])*-1