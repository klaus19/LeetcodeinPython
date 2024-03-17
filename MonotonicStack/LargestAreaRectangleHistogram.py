class Solution(object):

    def largest_rectangle_area(self,heights):
        """
        Calculates the largest area of a rectangle under a histogram.

        Args:
            heights: A list of non-negative integers representing the heights of a histogram.

        Returns:
            The maximum area of a rectangle under the histogram.
        """

        n = len(heights)
        next_smaller = [n] * n  # store indices of the next smaller element for each height
        previous_smaller = [-1] * n  # store indices of the previous smaller element for each height
        stack = []

        # Calculate previousSmaller and nextSmaller for each height
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                stack_top = stack.pop()
                next_smaller[stack_top] = i
            if stack:
                previous_smaller[i] = stack[-1]
            stack.append(i)

        # Find the maximum area
        max_area = 0
        for i in range(n):
            current_height = heights[i]
            width = next_smaller[i] - previous_smaller[i] - 1
            max_area = max(max_area, current_height * width)

        return max_area

if __name__ == '__main__':
    arr = [2,1,5,6,2,3]
    print(Solution().largest_rectangle_area(arr))