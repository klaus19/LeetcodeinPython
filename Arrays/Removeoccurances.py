from inspect import stack


class Solution(object):

    def remove_occurances(self, lt, k):

        i = 0
        while i < len(sorted(lt)):
            if lt[i] == k:
                lt.remove (lt[i])
            else:
                i += 1
        return lt

    def secondary_answer(self,nums,k):
        while k in nums:
            nums.remove(k)
        return nums


if __name__ == "__main__":
    p = [1, 1, 3, 4, 5, 5]
    k = 1
    print(Solution().secondary_answer(p,k))

   # print(Solution().remove_occurances(p, k))
