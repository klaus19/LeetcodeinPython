class Solution(object):

    def maxi_element(self, ltr):
        ltr.sort()
        max = ltr[0]

        for i in range(1, len(ltr)):
            if max < ltr[i]:
                max = ltr[i]

        return max


if __name__ == "__main__":
    p = Solution()
    lt = [3, 6, -1, 8, 9]
    print(p.maxi_element(lt))
