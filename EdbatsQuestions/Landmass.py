class Solution(object):

    def landmass(self, st, num):
        percentage = 148940000 / num * 100

        return str(st) + " " + "is" + " " + str(percentage) + "of total world mass!"


if __name__ == "__main__":
    s = "Russia"
    n = 17098242
    print(Solution().landmass(s, n))
