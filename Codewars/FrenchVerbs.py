class Solution(object):

    def to_imparfait(self, verb_phrase):
        """
    Input -  A subject + infinitive form of a verb.

    To conjugate a verb in the imparfait:
        - Drop the last two letters of the verb.
        - Replace it with the correct ending.
    See the table in the description for conjugations.
    """
        ltr = verb_phrase.split()

        if ltr[0] == 'Je' or ltr[0] == 'Tu':
            string = self.main_logic(ltr)
            return ltr[0] + " " + string + 'ais'
        elif ltr[0] == 'Il' or ltr[0] == 'Elle' or ltr[0] == 'On':
            string = self.main_logic(ltr)
            return ltr[0] + ' ' + string + 'ait'
        elif ltr[0] == 'Nous':
            string = self.main_logic(ltr)
            return ltr[0] + ' ' + string + 'ions'
        elif ltr[0] == 'Vous':
            string = self.main_logic(ltr)
            return ltr[0] + ' ' + string + 'iez'
        elif ltr[0] == 'Ils' or ltr[0] == 'Elles':
            string = self.main_logic(ltr)
            return ltr[0] + ' ' + string + 'aient'
        else:
            None

    def main_logic(self, ltr):
        string = ltr[- 1]  # get last element in a list
        string = str(string[:-2])
        return string


if __name__ == '__main__':
    s = 'Je Manger'
    st = 'Il livrer'
    t = 'Tu dormir'
    t1 = 'Elle coder'
    t2 = 'On parler'
    t3 = 'Nous aller'
    t4 = 'Vous partir'
    t5 = 'Ils jouer'
    t6 = 'Elles gagner'
print(Solution().to_imparfait(s))
print(Solution().to_imparfait(st))
print(Solution().to_imparfait(t))
print(Solution().to_imparfait(t1))
print(Solution().to_imparfait(t2))
print(Solution().to_imparfait(t3))
print(Solution().to_imparfait(t4))
print(Solution().to_imparfait(t5))
print(Solution().to_imparfait(t6))




