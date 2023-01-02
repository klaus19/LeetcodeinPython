class Solution(object):

    def get_middle(self,s):
        if len(s) ==1: return s[0]
        rev = ''
        if len(s)%2==0:   # s=middle, output = 'dd'

          s1 = str(s[0:len(s)-len(s)//2])
          s2 = str(s[len(s)-len(s)//2:len(s)])
          rev = s1[-1]+s2[0]
        else:
          mid = s[(len(s)-1)//2:(len(s)+2)//2]
          rev +=mid
        return rev

    def another_solution(self,s):
          index, odd = divmod(len(s), 2)
          return s[index] if odd else s[index - 1:index + 1]
if __name__ == "__main__":

    pt = 'mitdle'
    p = 'mid'
    print(Solution().get_middle(pt))
    print(Solution().get_middle(p))
