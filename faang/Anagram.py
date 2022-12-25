from collections import Counter


class Solution(object):

    def getAnagram(self, s1, s2):
        return Counter(s1) == Counter(s2)


if __name__ == '__main__':
    p = 'car'
    t = 'rac'

    print(Solution().getAnagram(p, t))
