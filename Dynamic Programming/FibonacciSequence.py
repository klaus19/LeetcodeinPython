
class Solution(object):

    def fibonacci(self,n):
        if n <=1:
            return n
        else:
            return self.fibonacci(n - 1)+ self.fibonacci(n - 2)

if __name__ == '__main__':
    n=5
    print(Solution().fibonacci(n))