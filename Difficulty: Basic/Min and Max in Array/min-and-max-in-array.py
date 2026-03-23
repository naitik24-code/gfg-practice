class Solution:
    def getMinMax(self, arr):
        mn=arr[0]
        mx=arr[0]
        for i in arr:
            if i<mn:
                mn=i
            if i>mx:
                mx=i
        return mn,mx