class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains = {}
        for i, num in enumerate(nums):
            if num in remains.values():
                return nums.index(target-num), i
            remains[num] = target-num
