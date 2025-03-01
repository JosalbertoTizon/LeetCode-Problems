class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        top_counts = []
        temp = list(counts.values())
        print(temp)
        for _ in range(k):
            maximum = temp[0]
            for i in temp:
                if i > maximum:
                    maximum = i
            temp.remove(maximum)
            top_counts.append(maximum)
        return [n for n, count in counts.items() if count in top_counts]
        
