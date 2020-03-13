from collections import Counter
class Solution(object):
    def isMajorityElement(self, nums, target):
        my_dict = Counter(nums)
        return (my_dict[target] > float(len(nums)/2))
