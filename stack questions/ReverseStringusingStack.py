class Solution(object):

    def doSomething(self,s):
        st = list(s)

        stack = []
        res = ""
        for i in range(len(st)-1,-1,-1):
            stack.append(st[i])
            res+=stack.pop()

        return res

if __name__ == "__main__":
    st = 'GeeksQuiz'
    print(Solution().doSomething(st))
