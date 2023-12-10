class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # split the string s into a list of words
        if len(pattern) != len(words):  # if the lengths don't match, there can't be a bijection
            return False
        char_words = {}
        


if __name__ == '__main__':
    s = "dog cat cat dog"
    pattern = "abba"
    print(Solution().wordPattern(pattern,s))