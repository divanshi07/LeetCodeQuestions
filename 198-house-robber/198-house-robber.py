class Solution:
    global dp
    dp=[]
    dp = [-1] * 101 
    def rob(self, nums: List[int]) -> int:
        global dp;
        if(len(nums)==0):
            return 0 
        if(len(nums)==1):
            return nums[0]
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(nums[i]+dp[i-2], dp[i-1])
        return dp[len(nums)-1]