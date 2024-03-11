class Solution(object):

    def nextSmallerIndex(self,nums):

        stack = []
        next_smaller = [-1]*len(nums)
        for i in range(len(nums)):

            while stack and nums[stack[-1]]>nums[i]:

                stack_top = stack.pop()

                next_smaller[stack_top] = i
            stack.append(i)

        return next_smaller

if __name__ == '__main__':
    arr = [13, 7, 6, 12]
    print(Solution().nextSmallerIndex(arr))




