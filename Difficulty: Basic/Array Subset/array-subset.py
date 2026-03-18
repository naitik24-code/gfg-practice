class Solution:
    # Function to check if b is a subset of a
    def isSubset(self, a, b):
        freq = {}

        for i in a:
            freq[i] = freq.get(i, 0) + 1

        for j in b:
            if j not in freq or freq[j] == 0:
                return False
            freq[j] -= 1

        return True
    
    
