class Solution:
    def search(self, k, arr):
        for i in range(len(arr)):
            if arr[i] == k:
                return i + 1   # 1-based index
        return -1