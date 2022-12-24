class Solution(object):

    def remove_vowels(self, s):
        vowels = 'aeiou'
        return ''.join([c for c in s if c not in vowels])


if __name__ == '__main__':
    lt = 'Hello world'
    print(Solution().remove_vowels(lt))
