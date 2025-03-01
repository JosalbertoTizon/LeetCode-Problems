class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        for s in strs:
            counts = {}
            for c in s:
                if c not in counts:
                    counts[c] = 0
                counts[c] += 1
            hash = tuple(sorted(counts.items()))
            if hash not in solution:
                solution[hash] = [s]
            else:
                solution[hash].append(s)
        return list(solution.values())

            
