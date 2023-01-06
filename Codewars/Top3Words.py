import re
from collections import Counter


class Solution(object):

    def top_3_words(self,text):
        # count the input, pass through a regex and lowercase it
        c =Counter(re.findall(r"[a-z']+",re.sub(r" '+ ", " ", text.lower())))

        # return the `most common` 3 items
        return [w for w ,_ in c.most_common(3) ]

if __name__ == "__main__":

    p = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"
    print(Solution().top_3_words(p))