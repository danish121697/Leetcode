class Solution(object):
    def numPairsDivisibleBy60(self, time):
        if len(time) == 0:
            return 0
        ans = 0
        mp = [0] * 60
        for t in time:
            ans += mp[(60 - t) % 60]
            mp[t % 60] += 1
        return ans
