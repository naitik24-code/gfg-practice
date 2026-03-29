class Solution:
    def countPartitions(self, arr, diff):
        total = sum(arr)
        
        # Check validity
        if (total + diff) % 2 != 0:
            return 0
        
        target = (total + diff) // 2
        
        # DP array
        dp = [0] * (target + 1)
        dp[0] = 1   # one way to make sum 0
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]