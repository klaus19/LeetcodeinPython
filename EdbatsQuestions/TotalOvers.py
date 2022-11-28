class Solution(object):

    def total_overs(self, balls):
        exact_overs = balls // 6
        remaining = balls % 6

        return f"{exact_overs}.{remaining}"


if __name__ == "__main__":
    p = Solution()
    ba = 945
    print(p.total_overs(ba))
