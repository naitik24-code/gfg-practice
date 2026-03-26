class Solution:
    def getOddOccurrence(self, arr):
        result = 0
        for num in arr:
            result^=num
        return result