class Solution(object):

    def consonant_count(self,s):

        vowels = 'aeiou'
        counter = 0
        for letter in s.lower():
            if (letter not in vowels) and letter.isalpha():
                counter += 1
        return counter

if __name__ == '__main__':
    pt = 'Taaaa'
    print(Solution().consonant_count(pt))