class Solution(object):

    def update_list(self, ltr, K):

        for i in range(0, len(ltr)):
            if i == K:
                del ltr[i]
                del ltr[0]
                del ltr[-1]

                return ltr


if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5]
    kt = 2
    print(Solution().update_list(lt, kt))
