class Solution:

    def bitwiseAND(self, no1, no2):
        ans = no1 & no2
        return ans

    def bitwiseOR(self, no1, no2):
        ans = no1 | no2
        return ans

    def bitwiseXOR(self, no1, no2):
        ans = no1 ^ no2
        return ans


if __name__ == "__main__":
    p = Solution()
    n1 = 7
    n2 = 12
    print(p.bitwiseAND(n1, n2))
    print(p.bitwiseOR(n1, n2))
    print(p.bitwiseXOR(n1, n2))
