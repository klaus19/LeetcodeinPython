from typing import Text


class Solution(object):

    def reversed(self, s):
        words = s.split()
        reversed_str = ''.join(reversed(words))
        return reversed_str


if __name__ == "__main__":
    p = Solution()
    st = "eM eM"
    print(p.reversed(st))
