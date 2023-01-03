

from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase
class Solution(object):


    def rot13(self,message):
        code = {letter: lowercase[(index + 13) % 26]
                for index, letter in enumerate(lowercase)}
        code.update((letter, uppercase[(index + 13) % 26])
                    for index, letter in enumerate(uppercase))
        return "".join(code.get(letter, letter) for letter in message)


if __name__ == "__main__":
    pt = "Hell"
    print(Solution().rot13(pt))