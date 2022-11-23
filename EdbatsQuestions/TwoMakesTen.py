class Solution:
    def twomakes10(self, no1, no2):

        if sum([no1, no2]) == 10:
            return True
        else:
            return False


if __name__ == "__main__":
    p = Solution()
    n1 = 9
    n2 = 1
    print(p.twomakes10(n1, n2))
