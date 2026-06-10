class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        char_count = {}
        max_length = -1

        for right in range(len(s)):
            # Add current character to hashmap
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # Shrink window if distinct characters > k
            while len(char_count) > k:
                char_count[s[left]] -= 1

                if char_count[s[left]] == 0:
                    del char_count[s[left]]

                left += 1

            # Update answer if exactly k distinct chars
            if len(char_count) == k:
                max_length = max(max_length, right - left + 1)

        return max_length