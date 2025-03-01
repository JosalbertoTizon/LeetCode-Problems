class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[0:m]
        if nums1 == []:
            nums1[:] = nums2[:]
        if nums2 != []:
            i = 0
            j = 0
            while i<m+j and j<n:
                print(nums1[i], nums2[j])
                if nums1[i] > nums2[j]:
                    nums1.insert(i, nums2[j])
                    i = i + 1
                    j = j + 1
                elif i != len(nums1)-1:
                    i = i + 1
                else:
                    nums1.append(nums2[j])
                    i = i + 1
                    j = j + 1
