class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest_seq = 1
        seq = 1
        values = set(nums)
        for num in values:
            if (num-1) not in values:
                seq = 1
                while num+1 in values:
                    num += 1
                    seq += 1
                longest_seq = max(longest_seq, seq)
        return longest_seq
        
