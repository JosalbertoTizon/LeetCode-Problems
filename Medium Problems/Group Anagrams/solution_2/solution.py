class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        for s in strs:
            sorted_s = sorted(s)
            if str(sorted_s) not in solution:
                solution[str(sorted_s)] = [s]
            else:
                solution[str(sorted_s)].append(s)
        return list(solution.values())

            
