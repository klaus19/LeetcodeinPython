class Solution(object):

    def reverse_words(self, sentence):
        ltr = sentence.split()
        new_str = ''
        for i in range(len(ltr)):
            new_str += " "+''.join(reversed(ltr[i]))
        return new_str


if __name__ == "__main__":
    st = "The quick brown fox jumps over the lazy dog."
    print(Solution().reverse_words(st))
