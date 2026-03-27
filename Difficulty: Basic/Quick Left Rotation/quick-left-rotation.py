class Solution:
    def leftRotate(self, arr, k):
        n=len(arr)
        k=k%n
        arr[:k]=arr[:k][::-1]
        arr[k:]=arr[k:][::-1]
        arr[:]=arr[::-1]
        return arr