class Solution(object):

    def min_xor_permutation(self,arr):
        n = len(arr)

        # If the number of elements is odd, the answer is 0
        if n % 2 == 1:
            return 0

        # If the number of elements is even, the answer is the XOR of all elements
        result = 0
        for num in arr:
            result ^= num

        return result

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().min_xor_permutation(nums))