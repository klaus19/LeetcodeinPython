class Solution(object):

    def first_non_repeating_letter(self,string):

        stringCopy = "".join([x.lower() for x in string])
        for s in stringCopy:
            if stringCopy.count(s) == 1:
                if s.isalpha():
                    if s in string: return s
                    if s.upper() in string: return s.upper()
                else:
                    return s
        return ""

    def second_method(self,s):  # using dictionary
        # Create a dictionary to store the count of each character
        char_count = {}

        # Iterate through each character in the string and add it to the dictionary
        for c in s:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

        # Find the first character that has a count of 1
        for c in s:
            if char_count[c] == 1:
                return c

        # If no characters have a count of 1, return None
        return None

    def third_method(self,s):
            # Create a set to store the characters that have been seen more than once
            repeating = set()

            # Create a queue to store the characters that have been seen only once
            non_repeating = []

            # Iterate through each character in the string
            for c in s:
                # If the character has already been seen, add it to the set of repeating characters
                if c in repeating:
                    continue
                # If the character has not been seen, add it to the queue of non-repeating characters
                elif c in non_repeating:
                    non_repeating.remove(c)
                    repeating.add(c)
                else:
                    non_repeating.append(c)

            # Return the first character in the queue of non-repeating characters, or None if the queue is empty
            return non_repeating[0] if non_repeating else None

    def first_non_repeating_letter(self,string):
        string_lower = string.lower()
        for i, letter in enumerate(string_lower):
            if string_lower.count(letter) == 1:
                return string[i]

        return ""

if __name__ == "__main__":
    pt = "hhello"
    print(Solution().first_non_repeating_letter(pt))


