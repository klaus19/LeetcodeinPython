class Solution(object):

    def easyWords(self,words,x):

        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
if __name__ == '__main__':
    x="e"
    words = ["leet","code"]
    print(Solution().easyWords(words,x))