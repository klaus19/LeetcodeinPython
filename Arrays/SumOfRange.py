class Solution(object):

    def SumOfR(self, num):
        total_sum = sum(range(1, num + 1))
        return total_sum


if __name__ == "__main__":
    p = Solution()
    n = 4
    print(p.SumOfR(n))
