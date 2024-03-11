class Solution(object):

    def consecutiveSame(self,st):

        i=0
        while i <len(st)-1:
            if st[i] == st[i+1]:
                del st[i:i+2]
                i = max(0,i-1)
            else:
                i+=1
        return len(st)

if __name__ == '__main__':
    st = "ab aa aa cc"
    print(Solution().consecutiveSame(st))
