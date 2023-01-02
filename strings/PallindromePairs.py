class Solution(object):

 def pallindrome_pairs(self,words):
    # Create an empty list to store the pairs
    pairs = []
   # Iterate over the words
    for i , word1 in enumerate(words):
     for j,word2 in enumerate(words):

 # Check if the concatenation of the two words is a palindrome
      if word1 + word2 == (word1 + word2)[::-1] and i != j:
        # Add the pair to the list
        pairs.append((word1, word2))

    return pairs

if __name__ == "__main__":
    pt =["race", "car", "level", "", "wow"]
    print(Solution().pallindrome_pairs(pt))



