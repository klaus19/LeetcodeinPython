class Solution(object):

    def calculate(self, num):
        count_no = 0
        while num > 0:
            num = num // 10
            count_no += 1

        return count_no


if __name__ == "__main__":
    p = Solution()
    n = 123
    print(p.calculate(n))
