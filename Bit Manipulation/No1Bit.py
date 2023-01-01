class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')


if __name__ == "__main__":
    pt = 0o00011
    print(Solution().hammingWeight(pt))
