class Solution:
    def threeSum(self, nums):
        answer = []
        nums.sort()
        for num_index, num in enumerate(nums):
            i = num_index + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] > -num:
                    j -= 1
                elif nums[i] + nums[j] < -num:
                    i += 1
                else:
                    triple = tuple(sorted([num, nums[i], nums[j]]))
                    answer.append(triple)
                    while i < j and nums[i + 1] == nums[i]:
                        i += 1
                    while i < j and nums[j - 1] == nums[j]:
                        j -= 1
                    i += 1
                    j -= 1
        return list(set(answer))
