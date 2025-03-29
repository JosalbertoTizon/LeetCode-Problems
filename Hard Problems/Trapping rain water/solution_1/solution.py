class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        i = 0 
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                for k in range(i+1, j):
                    total_water += (height[i] - height[k]) if height[i] > height[k] else 0
                    height[k] = max(height[k], height[i])
                i += 1
            elif height[i] > height[j]:
                for k in range(i+1, j):
                    total_water += (height[j] - height[k]) if height[j] > height[k] else 0
                    height[k] = max(height[k], height[j])
                j -= 1
            else:
                for k in range(i+1, j):
                   total_water += (height[i] - height[k]) if height[i] > height[k] else 0
                   height[k] = max(height[k], height[i])
                i += 1
                j -= 1
        return total_water
