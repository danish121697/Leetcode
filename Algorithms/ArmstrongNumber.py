class Solution(object):
    def isArmstrong(self, N):
        return N == sum([int(i)**len(str(N)) for i in str(N)])
