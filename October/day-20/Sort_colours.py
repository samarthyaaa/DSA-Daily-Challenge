class Solution(object):
    def sortColors(self, nums):
        maximum=max(nums)
        count=[0]*(maximum+1)
        for num in nums: #count each olour
            count[num]+=1
        i=0
        #put colours in correct order
        for num in range(maximum+1):
            while count[num]>0:
                nums[i]=num
                i+=1
                count[num]-=1
        return nums
        
