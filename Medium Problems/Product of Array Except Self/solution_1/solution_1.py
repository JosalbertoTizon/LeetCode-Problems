class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_products = [1, nums[0]]
        for i in range(1, len(nums) - 1):
            l_products.append(l_products[-1]*nums[i])
        r_products = [1, nums[-1]]
        for i in range(len(nums) - 2, 0, -1):
            r_products.append(r_products[-1]*nums[i])
        solution = []
        for i in range(len(nums)):
            solution.append(l_products[i]*r_products[len(nums)-i-1])
        return solution
