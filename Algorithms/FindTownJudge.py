class Solution(object):
    def findJudge(self, N, trust):
        lst = []
        if len(trust) == 0:
            return N
        d = {}
        for i in range(len(trust)):
            if trust[i][1] in d.keys():
                d[trust[i][1]] +=1
            else:
                trust[i][1] in d.keys()
                d[trust[i][1] ] = 1
        for i in range(len(trust)):    
            if trust[i][0] in d.keys():
                del(d[trust[i][0]])
        lst = list(d.items())
        for i in range(len(lst)):
            if lst[i][1] == N- 1:
                return lst[i][0]
            #lst[i][0]
        return - 1
