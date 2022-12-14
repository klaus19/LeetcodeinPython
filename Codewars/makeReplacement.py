class Solution(object):

    def makeSentence(self, parts):
        my_string = " "
        for a in parts:
            my_string = my_string + ' ' + a
        print(my_string)


if __name__ == "__main__":
    pt = ['tejas', ',','will','Khartude']
    print(Solution().makeSentence(pt))
