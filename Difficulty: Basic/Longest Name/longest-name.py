
class Solution:
    def longest(self, arr):
        longest_string=arr[0]
        max_length=len(arr[0])
        for s in arr:
            if len(s)>max_length:
                max_length=len(s)
                longest_string=s
        return longest_string