import collections


class Solution(object):

    def longestPalindrome(self, s: str) -> int:
        odd = 0  # whether or not we have any letters with an odd count
        ans = 0  # answer
        for count in collections.Counter(s).values():
            if count % 2 == 0:  # if we have an even amount of the letter
                ans += count  # we can use the letter
            else:
                odd = 1  # we have found an od
                ans += count - 1  # we can use all but the 1 of the letter
        return ans + odd  # if there was an odd amt of a letter, we can add that letter to the middle of our palindrome
if __name__ == "__main__":
    s = 'zzbaabcd'
    print(Solution().isPalindrome(s))