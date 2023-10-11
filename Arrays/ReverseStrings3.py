class Solution(object):
    def reverseWords(self, s):

        words = s.split()
        reverse_words = [word[::-1]for word in words]
        reverse_sentence = " ".join(reverse_words)

        return reverse_sentence

if __name__ == "__main__":
    ss = "my name is Tejas"
    print(Solution().reverseWords(ss))

