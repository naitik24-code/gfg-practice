class Solution:
    def binarySubstring(self, s):
        count_ones = s.count('1')
        return (count_ones * (count_ones - 1)) // 2