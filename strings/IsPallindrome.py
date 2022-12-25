class Solution(object):

    def isPallindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())

        # Reverse the string and compare it to the original
        return s == s[::-1]


if __name__ == '__main__':
    s = "racecar"
    print(Solution().isPallindrome(s))
