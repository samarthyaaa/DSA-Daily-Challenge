class Solution(object):
    def sortArrayByParity(self, nums):
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i): 
                if nums[j]%2 !=0 and nums[j+1] % 2 ==0: # put even numbers first
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
        return nums
