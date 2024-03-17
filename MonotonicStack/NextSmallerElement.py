
class Solution(object):

    def nextSmallerElement(self,arr):

        stack = []
        next_smaller = [-1]*len(arr)

        for i in range(len(arr)):

            while stack and arr[stack[-1]]>arr[i]:
                stack_top = stack.pop()

                next_smaller[stack_top] = arr[i]

            stack.append(i)
        return next_smaller

if __name__ == '__main__':
    arr = [13, 7, 6, 12]
    print(Solution().nextSmallerElement(arr))