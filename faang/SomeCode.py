class Solution(object):
    def listcheck(self, nums):
        nums.pop(0)
        nums.pop(-1)

    def ltr(self, no):
        for i in range(len(no)):
            n1 = max(no[:i - 1])
        return n1


if __name__ == "__main__":
    pt = [1, 2]
    l = [3, 6, 5]
    print(Solution().listcheck(pt))
    print(Solution().ltr(l))
