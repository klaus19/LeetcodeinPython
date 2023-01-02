class Solution(object):

    def reverse_str(self,st):

     words = st.split()

        # Reverse the words
     reversed_words = [word[::-1]for word in words]
     return "".join(reversed_words)

if __name__ == "__main__":
    pt = 'hello'
    print(Solution().reverse_str(pt))