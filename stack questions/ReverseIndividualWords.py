class Solution(object):

    def revrseIndi(self,st):
        result = ""
        stack = []


        words = st.split(" ")

        for word in words:
            i = len(word) - 1

            while i >= 0:
                stack.append(word[i])
                i -= 1

            result += "".join(stack)

            if word != words[-1]:
                result += " "

        return result

if __name__ == "__main__":
    res = "Hello world"
    print(Solution().revrseIndi(res))





