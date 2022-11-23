class Solution(object):

    def is_subset(self, tejas, pratik):
        if set(tejas)<=set(pratik):
            return True
        else:
            return False


if __name__ == "__main__":
    p = Solution()
    t = [1, 2, 3, 4, 5]
    s = [3, 4, 5]
    print(p.is_subset(t, s))
