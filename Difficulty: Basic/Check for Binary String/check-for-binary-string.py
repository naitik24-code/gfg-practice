class Solution:
    def isBinary(self, s):
        for ch in s:
            if ch != '0' and ch != '1':
                return False
        return True