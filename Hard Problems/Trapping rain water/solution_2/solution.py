class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        # First element of tallest_left: the tallest element to the left of height[1]      
        # Last element of tallest_left: the tallest element to the left of height[-2]
        tallest_left = [height[0]]
        for i in range(1, len(height)-2):
            if height[i] >= tallest_left[-1]:
                tallest_left.append(height[i])
            else:
                tallest_left.append(tallest_left[-1])
        # First element of tallest_right: the tallest element to the right of height[-2]
        # Last element of tallest_right: the tallest element to the right of height[1]     
        tallest_right = [height[-1]]
        for i in range(len(height)-2, 1, -1):
            if height[i] >= tallest_right[-1]:
                tallest_right.append(height[i])
            else:
                tallest_right.append(tallest_right[-1])
        tallest_right.reverse()
        i = 0 
        j = len(height) - 1
        for i in range(1, len(height)-1):
            limiter = min(tallest_left[i-1], tallest_right[i-1])
            water_above = (limiter - height[i]) if limiter > height[i] else 0
            total_water += water_above
        return total_water
