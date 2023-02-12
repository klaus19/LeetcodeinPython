class Solution(object):

    def add_dots(self,s):

         return '.'.join(s)

    def remove_dots(self,s):
        return s.replace('.','')


if __name__ == '__main__':

    s = "test"
    print(Solution().add_dots(s))
    print(Solution().remove_dots(s))

