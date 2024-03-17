class Solution(object):
    def longestPalindrome(self, s):
        char_dict = {}
        length = 0

        for char in s:
            char_dict[char] = 1 + char_dict.get(char, 0)

        for freq in char_dict.values():
            length += (freq // 2) * 2

        if any(freq % 2 == 1 for freq in char_dict.values()):
            length += 1

        return length

if __name__ == '__main__':
    s = 'abccccdd'
    print(Solution().longestPalindrome(s))