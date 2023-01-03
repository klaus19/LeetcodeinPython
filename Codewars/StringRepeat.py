class Solution(object):

    def repeat_str(self,repeat, string):
        rev=''
        i =0
        while i !=repeat:
            rev +=string
            i +=1
        return rev

if __name__ == '__main__':
    p = 'Hello'
    t =3
    print(Solution().repeat_str(t,p))