class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        top_counts = sorted(counts.values())[-k:]
        return [n for n, count in counts.items() if count in top_counts]
        
