from typing import List

class Solution:
    def isPerfect(self, arr: List[int]) -> bool:
        n = len(arr)
        
        for i in range(n // 2):
            if arr[i] != arr[n - i - 1]:
                return False
        
        return True