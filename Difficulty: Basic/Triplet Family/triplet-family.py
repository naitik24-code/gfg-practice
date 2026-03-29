class Solution:
    def findTriplet(self, arr):
        arr.sort()
        n = len(arr)
        
        for i in range(n - 1, 1, -1):  # fix c
            left = 0
            right = i - 1
            
            while left < right:
                if arr[left] + arr[right] == arr[i]:
                    return True
                elif arr[left] + arr[right] < arr[i]:
                    left += 1
                else:
                    right -= 1
        
        return False