import math


class Solution(object):

    def circle_square(self, radius, area):
        sq = math.sqrt(area)

        circumference_circle = 2 * 3.14 * radius
        perimeter_square = 4 * sq

        if circumference_circle > perimeter_square:
            return True
        else:
            return False


if __name__ == "__main__":
    p = Solution()
    r = 16
    ar = 625
    print(p.circle_square(r, ar))
