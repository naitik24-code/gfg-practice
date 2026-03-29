#User function Template for python3


class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        n=len(arr)
        mid=n//2
        left_sum=sum(arr[:mid])
        right_sum=sum(arr[mid:])
        return abs(left_sum-right_sum)