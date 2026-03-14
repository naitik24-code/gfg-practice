class Solution:
    def convertFive(self, n):
        n = str(n)
        n = n.replace('0', '5')
        return int(n)