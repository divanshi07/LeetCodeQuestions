class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pos=1
        neg=1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                pos = neg+1
            if nums[i]>nums[i-1]:
                neg = pos+1
        return max(pos,neg)