class Solution(object):

    def wordBreak(self, s, wordDict):
        new_str = ''
        for i in range(len(wordDict)):
            new_str = new_str + wordDict[i]

            if new_str == s:
                return True

        return False


if __name__ == "__main__":
    s = 'leetcode'
    st = 'applepenapple'
    words = ['leet', 'code']
    w = ["apple","pen"]
    print(Solution().wordBreak(s, words))
    print(Solution().wordBreak(st,w))
