class Solution(object):

    def longest_substring(self, s):

        # Set to store the characters in the current substring
        char_set = set()
        # Initialize maximum length
        max_len = 0
        # Initialize start and end indexes for the current substring
        start = 0
        end = 0
        # Loop through all characters in the string
        while end < len(s):
            # If the character is not in the set, add it and move the end index forward
            if s[end] not in char_set:
                char_set.add(s[end])
                end += 1
                # Update the maximum length
                max_len = max(max_len, end - start)
            # If the character is already in the set, remove the character at the start index and move the start
            # index forward
            else:
                char_set.remove(s[start])
                start += 1
        # Return the maximum length
        return max_len


if __name__ == "__main__":
    pt = "abcab"
    print(Solution().longest_substring(pt))
