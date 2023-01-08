import math


class Solution(object):
    def max_df(self,a_n: int) -> int:
        return (math.isqrt(8*a_n)-1) // 2

if __name__ == "__main__":
    p = 7
    print(Solution().max_df(p))