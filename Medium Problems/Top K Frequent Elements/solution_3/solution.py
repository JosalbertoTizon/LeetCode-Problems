class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [set() for _ in range(len(nums))]
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
                buckets[0].add(num)
            else:
                buckets[counts[num]-1].remove(num)
                buckets[counts[num]].add(num)
            counts[num] += 1
        return [num for l in buckets for num in l][-k:]
        
