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

        while end < len(s):

            if s[end] not in char_freq:
                count += 1

            char_freq[s[end]] = char_freq.get(s[end], 0) + 1

            while count > k:
                char_freq[s[start]] -= 1

                if char_freq[s[start]] == 0:
                    count -= 1
                start += 1
            # Update the maximum length if the current window is larger
            max_len = max(max_len, end - start + 1)
            # Move the end index forward
            end += 1
        # Return the maximum length
        return max_len

if __name__ == '__main__':
    s = "ABAB"
    k=2
    print(Solution().characterReplacement(s,k))