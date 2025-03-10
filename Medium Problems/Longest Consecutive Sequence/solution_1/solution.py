class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest_seq = 1
        seq = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                seq += 1
                continue
            longest_seq = max(longest_seq, seq)
            seq = 1
        longest_seq = max(longest_seq, seq)
        return longest_seq
        
