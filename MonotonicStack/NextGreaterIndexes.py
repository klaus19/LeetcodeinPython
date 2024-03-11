class Solution(object):
    def find_next_greater_indexes(self,arr):
        # initialize an empty stack
        stack = []

        # initialize nextGreater array, this array holds the output
        # initialize all the elements as -1 (invalid value)
        next_greater = [-1] * len(arr)

        # iterate through all the elements of the array
        for i in range(len(arr)):

            # while loop runs until the stack is not empty AND
            # the element represented by stack top is STRICTLY SMALLER than the current element
            # This means, the stack will always be monotonic non-increasing (type 4)
            while stack and arr[stack[-1]] < arr[i]:
                # pop out the top of the stack, it represents the index of the item
                stack_top = stack.pop()

                # as given in the condition of the while loop above,
                # the nextGreater element of stackTop is the element at index i
                next_greater[stack_top] = i

            # push the current element
            stack.append(i)

        return next_greater



if __name__ == '__main__':
    # Example usage:
    n = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
    print(Solution().find_next_greater_indexes(n))
