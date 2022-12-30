class Solution(object):

    def max_subArray(self, arr):
        curr_max = arr[0]
        max_mum = arr[0]

        for i in range(1, len(arr)):
            curr_max = max(arr[i], curr_max + arr[i])
            max_mum = max(curr_max, max_mum)
        return max_mum


if __name__ == "__main__":
    pt = [2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().max_subArray(pt))
