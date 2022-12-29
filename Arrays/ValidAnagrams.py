from collections import Counter


class Solution(object):

    def valid_anagram(self, s, t):
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    p = "anagram"
    t = "nagaram"
    s = "rat"
    q = "car"
    print(Solution().valid_anagram(p, t))
    print(Solution().valid_anagram(s,q))