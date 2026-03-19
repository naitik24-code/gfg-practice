class Solution:
    def leftRotate(self, arr, d):
        n = len(arr)
        d = d % n
        
        temp = arr[:d]          # store first d elements
        for i in range(d, n):
            arr[i-d] = arr[i]   # shift elements left
        
        for i in range(d):
            arr[n-d+i] = temp[i]  # place stored elements at end