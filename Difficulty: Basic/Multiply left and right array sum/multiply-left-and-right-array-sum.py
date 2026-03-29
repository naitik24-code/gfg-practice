class Solution:
    def multiply(self, arr):
        n = len(arr)
        mid = n // 2
        
        left_sum = sum(arr[:mid])
        right_sum = sum(arr[mid:])
        
        return left_sum * right_sum