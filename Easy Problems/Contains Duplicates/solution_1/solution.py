class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num = None
        for x in nums:
            if x == num:
                return True
            num = x
        return False
        
