class Solution(object):
    def intersection(self, nums1, nums2):
        ans=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                if nums1[i] not in ans:
                    ans.append(nums1[i])
        return ans
time complexity : O(n*m)
