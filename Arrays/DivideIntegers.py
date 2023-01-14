import sys
class Solution(object):

    def divide_integer(self,dividend,divisor):

        res = dividend/divisor
        return round(res)

if __name__ == "__main__":
    p=7
    t=-3
    dividend =10
    divisor =3
    print(sys.version)
    print(Solution().divide_integer(p,t))
    print(Solution().divide_integer(dividend,divisor))