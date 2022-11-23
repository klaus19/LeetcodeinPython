from collections import Counter


class Solution(object):

    def check_isogram(self, str1):

        freq = Counter(str1)
        if len(freq) == len(str1):
            return True
        else:
            return False


if __name__ == "__main__":
    p = Solution()
    st = "Algorism"
    print(p.check_isogram(st))
