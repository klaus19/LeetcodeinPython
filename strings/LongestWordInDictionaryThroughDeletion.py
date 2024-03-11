class Solution(object):
    def findLongestWord(self, s, d):

        # Sort the dictionary by length and lexicographically
        d.sort(key=lambda x: (-len(x), x))

        # Traverse through the dictionary
        for word in d:
            i = 0
            # Traverse through the string s
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
                    # If we have found all the characters in the word, break the loop
                    if i == len(word):
                        break
            # If we have found all the characters in the word, return the word
            if i == len(word):
                return word
        return ""

if __name__ == "__main__":
    st = "abpcplea"
    dictionary = ["ale","apple","monkey","plea"]
    print(Solution().findLongestWord(st, dictionary))