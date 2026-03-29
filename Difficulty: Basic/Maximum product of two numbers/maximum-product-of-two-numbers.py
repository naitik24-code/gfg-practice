class Solution:
    def maxProduct(self, arr):
        max1 = max2 = 0
        
        for num in arr:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        
        return max1 * max2