import datetime


class Solution(object):

    def make_readable(self,s):
        return f'{s // 3600:02}:{s // 60 % 60:02}:{s % 60:02}'

if __name__ == "__main__":
    t = 86399
    print(Solution().make_readable(t))