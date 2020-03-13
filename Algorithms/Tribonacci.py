class Solution(object):
    def tribonacci(self, n):
        n0 = 0
        n1 = 1
        n2 = 1
        count = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            for i in (range(n-2)):
                n3 = n0+ n1 + n2
                n0 = n1
                n1 = n2
                n2 = n3
                count = n3
            return count
