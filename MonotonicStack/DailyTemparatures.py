class Solution(object):
    def dailyTemperatures(self, temperatures):

        stack = []
        next_greater = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stack_top = stack.pop()
                # i - stack_top is the number of days to wait
                next_greater[stack_top] = i - stack_top

            stack.append(i)

        return next_greater

if __name__ == '__main__':

    temps = [73,74,75,71,69,72,76,73]
    print(Solution().dailyTemperatures(temps))