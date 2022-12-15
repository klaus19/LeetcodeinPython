class Solution(object):

    def ignoreDuplicates(self, array):
        sum = array[0]
        i = 1
        while i < len(array):
            sum ^= array[i]
            i += 1
        return sum


if __name__ == "__main__":
    ltr = [3, 2, 3, 4]
    print(Solution().ignoreDuplicates(ltr))
