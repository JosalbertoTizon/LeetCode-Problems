class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        while True:
            if i<0:
                nums1[:j+1] = nums2[:j+1]
                break
            if j<0:
                break
            if nums1[i] > nums2[j]:
                nums1[i+j+1] = nums1[i]
                i=i-1
            else:
                nums1[i+j+1] = nums2[j]
                j=j-1
