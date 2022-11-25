class Solution(object):

    def count_true(self, values_count=[]):

        am = 0
        for i in values_count:
            if values_count[i] == True:
                am + 1
                return am
            else:
                pass


if __name__ == '__main__':
    p = Solution()
    ltr = [False, True, True, True]
    print(p.count_true(ltr))
