class Solution(object):
    def removeAnagrams(self, words):


        count_word = {}
        res=[[]]

        for word in words:
            count_word = 1+count_word.get(word,0)


        for idx in count_word.items():
            if idx not in count_word:
                res.append([idx])
            else:
                res.remove([idx])
         return res

if __name__ == '__main__':
    words = ["abba","baba","bbaa","cd","cd"]
    print(Solution().removeAnagrams(words))