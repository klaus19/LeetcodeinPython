class Solution(object):

    def longest_substring_length(self,s):
        if not s:
            return 0

        char_set = set()
        max_length = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1

        return max_length


if __name__ == '__main__':
    # Test the function
    s = "abcabcbb"
    print(Solution().longest_substring_length(s))  # Output: 3 (the longest substring without repeating characters is "abc")
