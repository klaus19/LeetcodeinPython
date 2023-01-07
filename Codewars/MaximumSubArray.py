class Solution(object):

    def max_sequence(self,arr):
        max, curr = 0, 0
        for x in arr:
            curr += x
            if curr < 0: curr = 0
            if curr > max: max = curr
        return max

if __name__ == "__main__":

    pt = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    tr = []
    print(Solution().max_sequence(pt))
    print(Solution().max_sequence(tr))