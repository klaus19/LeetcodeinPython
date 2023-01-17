class Solution(object):

    def productExceptSelf(self,nums):
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        result = [1] * n
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        for i in range(n):
            result[i] = left_product[i] * right_product[i]
        return result


if __name__ == "__main__":
    lt = [2,3,4]
    print(Solution().productExceptSelf(lt))