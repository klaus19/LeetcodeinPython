class Solution(object):

    def reverse_word(self,s):
        # Split the string into words
        words = s.split()

        # Reverse the order of the words
        reversed_words = words[::-1]

        # Join them
        reversed_string = " ".join(reversed_words)

        return reversed_string

if __name__ == '__main__':
    str = "the sky is blue"
    print(Solution().reverse_word(str))
