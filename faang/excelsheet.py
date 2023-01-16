#Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.
class Soluttion(object):

    def titleToNumber(self, columnTitle):
        res = 0
        val = [i for i in range(1, 27)]
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        d = dict(zip(letters, val))
        for ch in s:
            res = res * 26 + d[ch]
        return res

if __name__ == '__main__':
    s='AA'
    print(Soluttion().titleToNumber(s))

