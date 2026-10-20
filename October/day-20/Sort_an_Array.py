class Solution(object):
    def sortColors(self, nums):
        count=[0]*2
        for num in nums: 
            count[num]+=1
        i=0
        for num in range(2):
            while count[num]>0:
                nums[i]=num
                i+=1
                count[num]-=1
        return nums
