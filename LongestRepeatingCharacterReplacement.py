class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_freq = 0  # The frequency of the most frequent character in the current window
        char_count = {}  # Frequency map for the characters in the current window
        
        left = 0  # Initialize left pointer of the window
        for right in range(len(s)):  # Expand the window by moving the right pointer
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_freq = max(max_freq, char_count[s[right]])
            
            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1  # Shrink the window from the left
            
            # Update max_length if the current window size is larger
            max_length = max(max_length, right - left + 1)
        
        return max_length