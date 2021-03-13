class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for cnt,num in enumerate(nums):
            if target-num in dic:
                return cnt,dic[target-num]
            dic[num]=cnt
        
        
