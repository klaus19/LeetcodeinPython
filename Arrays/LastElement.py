class Solution(object):
    def last(self, li):
        for i in range(len(li)):
            last = li[-1]
        return last


if __name__ == "__main__":
    p = Solution()
    lion = ['A', 1, 4, 'B']
    print(p.last(lion))
