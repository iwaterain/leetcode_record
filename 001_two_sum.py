class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for id, num in enumerate(nums):
            rest = target-num
            if rest in dic:
                return[id,dic[rest]]
            dic[num]=id
