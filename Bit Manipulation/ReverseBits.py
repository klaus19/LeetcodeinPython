class Solution(object):

    def reversebITS(self, n):

        return int(bin(n)[:1:-1], 2)

if __name__ == "__main__":
    t = 1234
    print(Solution().reversebITS(t))