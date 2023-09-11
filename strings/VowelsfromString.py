class Solution(object):

    def removeVowels(self, s):

        vowels = "aeiouAEIOU"

        new_str = ""
        for char in range(len(s)):
            if s[char] in vowels:
                continue
            else:
                new_str+=s[char]

        return new_str

if __name__ == "__main__":
    S = "leetcodeisacommunityforcoders"
    print(Solution().removeVowels(S))

