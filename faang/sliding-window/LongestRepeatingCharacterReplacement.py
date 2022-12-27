class Solution(object):
    def characterReplacement(self, s, k):
        # Initialize the start and end indices of the sliding window
        start = 0
        end = 0
        # Initialize a counter to track the number of distinct characters in the window
        count = 0
        # Initialize the maximum length
        max_len = 0
        # Initialize a map to store the frequency of each character in the window
        char_freq = {}
        # Loop through the characters in the string
        while end < len(s):
            # If the character is not in the current window, increment the count
            if s[end] not in char_freq:
                count += 1
            # Increment the frequency of the character
            char_freq[s[end]] = char_freq.get(s[end], 0) + 1
            # While the number of distinct characters is greater than 2, move the start index forward
            while count > 2:
                char_freq[s[start]] -= 1
                # If the character at the start index is no longer in the window, decrement the count
                if char_freq[s[start]] == 0:
                    count -= 1
                start += 1
            # Update the maximum length if the current window is larger
            max_len = max(max_len, end - start + 1)
            # Move the end index forward
            end += 1
        # Return the maximum length
        return max_len


if __name__ == "__main__":
    s = "AABABBA"
    k = 1

    print(Solution().characterReplacement(s, k))
