class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains = {}
        for num in nums:
            remains[num] = target-num
        for i in nums:
            if i in remains.values():
                if i==target-i and nums.count(i)==1:
                    continue
                index = nums.index(i)
                nums[nums.index(i)] = None
                return index, nums.index(remains[i])
