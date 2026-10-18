class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        last = m + n - 1
      
        while i >= 0 and j >= 0:  # Compares elements from the end
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1

            last -= 1

        while j >= 0:# Copy remaining nums2 elements
            nums1[last] = nums2[j]
            j -= 1
            last -= 1
