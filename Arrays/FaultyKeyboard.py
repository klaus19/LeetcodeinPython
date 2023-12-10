class Solution(object):
    def finalString(self, s):
        ls = list(s)
        st=[]
        for char in ls:

            if char!="i":
                st.append(char)
            else:
                st.reverse()

        return ''.join(st)

if __name__ == '__main__':
    ss = "string"
    print(Solution().finalString(ss))

