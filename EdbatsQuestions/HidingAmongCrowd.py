class Solution(object):

    def find_crowd(self, st):
        lo = ""
        for i in range(len(st)):
            if st[i].islower():
                lo += st[i]
        return lo


if __name__ == "__main__":
    p = Solution()
    s = "ABcASFatBD"
    print(p.find_crowd(s))
