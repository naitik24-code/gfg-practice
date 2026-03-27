class Solution:
    def check_elements(self, arr, n, A, B):
        s = set(arr)
        
        for num in range(A, B + 1):
            if num not in s:
                return False
                
        return True